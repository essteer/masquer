import random
import re

VERSION_RE = re.compile(r"Chrome\/(\d+\.\d+\.\d+\.\d+)")

def select_data(sample_space: list[str], weights: list[float]) -> str:
    """
    Makes a weighted random selection from a given sample space

    Parameters
    ----------
    sample_space: list[str]
        options to randomly select from

    weights: list[float]
        weight per sample in sample_space

    Returns
    -------
    selection: str
        selection from sample_space
    """
    selection = random.choices(sample_space, weights=weights, k=1)

    return selection[0]

def select_ch_ua(user_agent: str, sec_ch_uas: dict) -> dict:
    """
    Returns the Chrome sec-ch-ua from a user-agent string
    """
    
    # Get the obvious two, mobile and platform
    sec_dict = {}
    if is_mobile(user_agent):
        sec_dict["sec-ch-ua-mobile"] = "?1"
    else:
        sec_dict["sec-ch-ua-mobile"] = "?0"
   
    sec_dict["sec-ch-ua-platform"] = get_platform(user_agent)
    
    # Now for the rest - the actual UA
    # This is three steps:
    # - Identify the version of Chrome from user agent
    # - Identify browser name from user agent
    # - replace "Google Chrome" with browser name
    try:
        version = VERSION_RE.search(user_agent)
        sec_ch_ua = sec_ch_uas[version.group(1)]
        sec_ch_ua = sec_ch_ua.replace('Google Chrome', find_browser_name(user_agent))
        sec_dict["sec-ch-ua"] = sec_ch_ua
        return sec_dict
    except:
        return None
    

def is_mobile(user_agent: str) -> bool:
    """
    Checks whether a user-agent is mobile
    Returns True if mobile, else False
    """    
    return "Mobile" in user_agent

def get_platform(user_agent: str) -> str:
    """
    Returns the platform of a user-agent
    """
    if "Android" in user_agent:
        return '"Android"'
    elif "Linux x86_64" in user_agent:
        return '"Linux"'
    elif "Windows NT" in user_agent:
        return '"Windows"'
    elif "Macintosh" in user_agent:
        return '"macOS"'
    elif "iPhone" in user_agent:
        return '"iOS"'
    else:
        return "Unknown"
    
def find_browser_name(user_agent: str) -> str:
    """
    Returns the browser name from a user-agent string
    """
    if "Brave" in user_agent:
        return "Brave"
    elif "Edg" in user_agent:
        return "Microsoft Edge"
    elif "OPR" in user_agent:
        return "Opera"
    elif "SamsungBrowser" in user_agent:
        return "Samsung Internet"
    elif "OPX" in user_agent:
        return "Opera GX"
    else:
        return "Google Chrome"