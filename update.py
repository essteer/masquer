import base64
import json
import os
import re
import requests
import sys
from bs4 import BeautifulSoup
from src.logging_config import setup_logging, get_logger


setup_logging(__name__)
logger = get_logger(__name__)

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
UTILS_DIR = os.path.join(ROOT_DIR, "src", "masquer", "utils")
VERSION_RE = re.compile(r"Chrome\/(\d+\.\d+\.\d+\.\d+)")


def update_useragents() -> bool:
    """Gets latest user-agent stats and saves them to JSON file"""
    try:
        response = requests.get("https://www.useragents.me/")
        html = BeautifulSoup(response.content, "html.parser")
        div = html.find("div", id="most-common-desktop-useragents-json-csv")
        textarea = div.find(string="JSON").find_next("textarea").contents[0]

        json_string = json.loads(textarea)
        with open(os.path.join(ASSETS_DIR, "useragents.json"), "w") as f:
            json.dump(json_string, f)

        logger.info("Fetched user-agent data")
        return True

    except Exception as e:
        logger.error(f"Error fetching user-agent data: {e}")
        return False


def update_referers() -> bool:
    """Gets latest referer stats and saves them to JSON file"""
    SITES = {
        "baidu": "https://www.baidu.com",
        "bing": "https://bing.com",
        "duckduckgo": "https://duckduckgo.com",
        "google": "https://www.google.com",
        "yahoo!": "https://search.yahoo.com",
        "yandex": "https://yandex.com",
    }
    try:
        response = requests.get(
            "https://gs.statcounter.com/search-engine-market-share/desktop/worldwide"
        )
        html = BeautifulSoup(response.content, "html.parser")

        table = html.find("table", class_="stats-snapshot")
        tbody = table.find("tbody")

        search_engines = []
        market_shares = []

        for row in tbody.find_all("tr"):
            search_engine = row.find("th")
            market_share = row.find("span", class_="count")
            if search_engine and market_share:
                search_engines.append(search_engine.text.strip().lower())
                market_share_text = market_share.text.strip()
                market_shares.append(float(market_share_text))

        output = []
        for i in range(len(search_engines)):
            output.append({"ref": SITES[search_engines[i]], "pct": market_shares[i]})
        # Convert to JSON and save
        with open(os.path.join(ASSETS_DIR, "referers.json"), "w") as f:
            json.dump(output, f)

        logger.info("Fetched referer data")
        return True

    except Exception as e:
        logger.error(f"Error fetching referer data: {e}")
        return False


def extract_data(json_file_path: str) -> dict | list[dict]:
    """
    Loads data from JSON file

    Parameters
    ----------
    json_file_path: str
        path to JSON file

    Returns
    -------
    data: dict | list
        data loaded from JSON file
    """
    with open(json_file_path, "r") as f:
        data = json.load(f)
    return data

def update_sec_ch_ua() -> bool:
    """Gets latest referer stats and saves them to JSON file"""
    REPO_OWNER = "fa0311"
    REPO_NAME = "latest-user-agent"
    BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
    FILE_PATH = "header.json"
    
    latest_commits = get_latest_commits(f"{BASE_URL}/commits")
    sec_ch_uas = {}
    logger.info("Fetched sec-ch-ua data")
    for commit in latest_commits:
        file_content = get_file_content_at_commit(f"{BASE_URL}/contents/{FILE_PATH}", commit)
        version, sec_ch_ua = extract_sec_ch_ua(file_content)
        if sec_ch_ua:
            sec_ch_uas[version] = sec_ch_ua
    json_string = json.dumps(sec_ch_uas)
    with open(os.path.join(ASSETS_DIR, "sec_ch_ua.json"), "w") as f:
        json.dump(json_string, f)
    return True
    

def get_latest_commits(url: str):
    """Fetch the latest 5 commits that modified the file."""
    FILE_PATH = "header.json"
    params = {
        "path": FILE_PATH,
        "per_page": 10  # Limit to the latest 5 commits
    }
    response = requests.get(url,  params=params)
    response.raise_for_status()
    return [commit["sha"] for commit in response.json()]


def get_file_content_at_commit(url: str, commit_sha: str):
    """Fetch the file content at a specific commit."""
    params = {
        "ref": commit_sha
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    content = response.json()["content"]
    # Decode the base64-encoded content
    return base64.b64decode(content).decode("utf-8")

def extract_sec_ch_ua(json_content):
    """Extract the 'sec-ch-ua' value from the JSON content."""
    data = json.loads(json_content)
    user_agent = data.get("chrome", {}).get("user-agent", None)
    if not user_agent:
        return None, None
    version = VERSION_RE.search(user_agent)
    return version.group(1), data.get("chrome", {}).get("sec-ch-ua", None)

def update_assets() -> bool:
    """
    Converts JSON assets into Python variables
    Run to sync data in src/utils/assets.py after updating JSON assets

    Returns True if successful else False
    """
    try:
        header_data = extract_data(os.path.join(ASSETS_DIR, "header.json"))
        referer_data = extract_data(os.path.join(ASSETS_DIR, "referers.json"))
        useragent_data = extract_data(os.path.join(ASSETS_DIR, "useragents.json"))
        sec_ch_ua_data = extract_data(os.path.join(ASSETS_DIR, "sec_ch_ua.json"))

        referers = [obj["ref"] for obj in referer_data]
        referer_weights = [obj["pct"] for obj in referer_data]

        useragents = [obj["ua"] for obj in useragent_data]
        useragent_weights = [obj["pct"] for obj in useragent_data]

        with open(os.path.join(UTILS_DIR, "assets.py"), "a") as f:
            f.seek(0)
            f.truncate()
            f.write("HEADER_DATA = " + str(header_data))
            f.write("\n")
            f.write("REFERERS = " + str(referers))
            f.write("\n")
            f.write("REFERER_WEIGHTS = " + str(referer_weights))
            f.write("\n")
            f.write("USERAGENTS = " + str(useragents))
            f.write("\n")
            f.write("USERAGENT_WEIGHTS = " + str(useragent_weights))
            f.write("\n")
            f.write("SEC_CH_UA = " + str(sec_ch_ua_data))
            f.write("\n")

        logger.info("Saved user-agent, referer and sec-ch-ua JSON data to assets.py")
        return True

    except FileNotFoundError:
        logger.error("Asset update error: JSON assets not found")
        return False

    except Exception as e:
        logger.error(f"Asset update error: {type(e)}: {e}")
        return False


if __name__ == "__main__":
    ua = update_useragents()
    rf = update_referers()
    sec_ch_ua = update_sec_ch_ua()
    
    if ua and rf and sec_ch_ua:
        assets_updated = update_assets()
        if assets_updated:
            sys.exit(0)
        else:
            sys.exit(2)
    else:
        sys.exit(3)
