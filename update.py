import json
import os
import requests
from bs4 import BeautifulSoup


# Get absolute path for root directory
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
# Path to assets and utils directories
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
UTILS_DIR = os.path.join(ROOT_DIR, "src", "masquer", "utils")


def update_useragents() -> bool:
    """
    Gets latest useragent stats
    Saves stats to JSON file
    """
    try:
        response = requests.get("https://www.useragents.me/")
        html = BeautifulSoup(response.content, "html.parser")
        # Find div for desktop stats
        div = html.find("div", id="most-common-desktop-useragents-json-csv")
        textarea = div.find(string="JSON").find_next("textarea").contents[0]
        # Convert to JSON and save
        json_string = json.loads(textarea)
        with open(os.path.join(ASSETS_DIR, "useragents.json"), "w") as f:
            json.dump(json_string, f)

        return True

    except Exception as e:
        print(f"Error fetching useragent data: {e}")
        return False


def update_referers() -> bool:
    """
    Gets latest referer stats
    Saves stats to JSON file
    """
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
        # Loop through <tbody> rows
        for row in tbody.find_all("tr"):
            # Find <th> element (search engine name)
            search_engine = row.find("th")
            # Find <span> element with class "count" (market share)
            market_share = row.find("span", class_="count")
            # Confirm both elements found
            if search_engine and market_share:
                # Extract text content from <th> element
                search_engines.append(search_engine.text.strip().lower())
                # Convert market share text to float
                market_share_text = market_share.text.strip()
                market_shares.append(float(market_share_text))

        output = []
        for i in range(len(search_engines)):
            output.append({"ref": SITES[search_engines[i]], "pct": market_shares[i]})
        # Convert to JSON and save
        with open(os.path.join(ASSETS_DIR, "referers.json"), "w") as f:
            json.dump(output, f)

        return True

    except Exception as e:
        print(f"Error fetching referer data: {e}")
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


def update_assets() -> bool:
    """
    Converts JSON assets into Python variables
    Run to sync data in src/utils/assets.py after updating JSON assets

    Returns True if successful else False
    """
    try:
        # Get JSON file data
        header_data = extract_data(os.path.join(ASSETS_DIR, "header.json"))
        referer_data = extract_data(os.path.join(ASSETS_DIR, "referers.json"))
        useragent_data = extract_data(os.path.join(ASSETS_DIR, "useragents.json"))

        referers = [obj["ref"] for obj in referer_data]
        referer_weights = [obj["pct"] for obj in referer_data]

        useragents = [obj["ua"] for obj in useragent_data]
        useragent_weights = [obj["pct"] for obj in useragent_data]

        # Save JSON content to assets.py
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

        return True

    except FileNotFoundError:
        print("Error: JSON asset(s) missing")
        return False

    except Exception as e:
        print(f"{type(e)}: {e}")
        return False


if __name__ == "__main__":
    ua = update_useragents()
    rf = update_referers()
    if ua and rf:
        assets_updated = update_assets()
        if not assets_updated:
            print("Failed to update assets.py")
        else:
            print("Update successful")
    else:
        print("Failed to update JSON assets")
