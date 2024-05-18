import json
from utils.assets import REFERERS, REFERER_WEIGHTS, USERAGENTS, USERAGENT_WEIGHTS
from utils.select import select_data


def get_response() -> str:
    """
    Prepares and returns header data
    
    Returns
    -------
    json_header: str
        JSON-formatted header data
    """
    # Get attributes
    referer = select_data(REFERERS, REFERER_WEIGHTS)
    useragent = select_data(USERAGENTS, USERAGENT_WEIGHTS)
     
    # Initialise header data
    header_data = {}
    header_data["Referer"] = referer
    header_data["User-Agent"] = useragent 
    
    json_header = json.dumps(header_data)
    
    return json_header

