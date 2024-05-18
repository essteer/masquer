import json


def extract_data(json_file_path: str) -> list[dict]:
    """
    Extracts data from JSON file and returns Python list
  
    Parameters
    ----------
    json_file_path: str
        path to JSON file
  
    Returns
    -------
    extracted_data: list
        data from JSON file
    """
    with open(json_file_path, "r") as f:
        data = json.load(f)
    
    extracted_data = []
    for item in data:
        extracted_data.append(item)
  
    return extracted_data


def update_assets() -> bool:
    """
    Converts JSON assets into Python variables
    Run to sync data after updating JSON assets
    
    Returns True if successful else False
    """
    try:
        referer_data = extract_data("../assets/referers.json")
        # Create lists of data and weights
        referers = [obj["ref"] for obj in referer_data]
        referer_weights = [obj["pct"] for obj in referer_data]
        
        useragent_data = extract_data("../assets/useragents.json")
        # Create lists of data and weights
        useragents = [obj["ua"] for obj in useragent_data]
        useragent_weights = [obj["pct"] for obj in useragent_data]
        
        # Save JSON content to assets.py
        with open("assets.py", "a") as f:
            f.seek(0)
            f.truncate()
            f.write("# -*- coding: utf-8 -*-")
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
