import json
import os


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
        # Get absolute path for root directory
        root_dir = os.path.abspath(os.path.dirname(__file__))
        # Path to assets and utils directories
        assets_dir = os.path.join(root_dir, "assets")
        utils_dir = os.path.join(root_dir, "src", "masquer", "utils")

        # Get JSON file data
        header_data = extract_data(os.path.join(assets_dir, "header.json"))
        referer_data = extract_data(os.path.join(assets_dir, "referers.json"))
        useragent_data = extract_data(os.path.join(assets_dir, "useragents.json"))

        referers = [obj["ref"] for obj in referer_data]
        referer_weights = [obj["pct"] for obj in referer_data]

        useragents = [obj["ua"] for obj in useragent_data]
        useragent_weights = [obj["pct"] for obj in useragent_data]

        # Save JSON content to assets.py
        with open(os.path.join(utils_dir, "assets.py"), "a") as f:
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


update = update_assets()
if not update:
    print("Failed to update assets.py")
else:
    print("Asset update successful")
