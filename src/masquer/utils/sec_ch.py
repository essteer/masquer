from .assets import (SEC_CH_UA, HEADER_DATA)
import re
def append_sec_ch(user_agent: str, headers: dict) -> str:
    if(user_agent.find('Chrome') == -1):
        return headers
    platform = get_platform(user_agent)
    headers['sec-ch-ua-platform'] = platform
    headers['sec-ch-ua-mobile'] = "?1" if is_mobile(user_agent) else "?0"
    headers['sec-ch-ua'] = find_sec_ch(get_chrome_version(user_agent)).replace('%c', get_browser(user_agent))
    return headers
    
    

def find_sec_ch(version: str) -> str:
    if version in SEC_CH_UA:
        return SEC_CH_UA[version]
    else:
        return "Not Found"
    
def get_browser(user_agent: str) -> str:
    if('Edg' in user_agent):
        return 'Microsoft Edge'
    elif('OPR' in user_agent):
        # TODO: Opera have a custom sec-ch-ua for mobile version...
        return 'Opera'
    else:
        return 'Google Chrome'

def get_platform(user_agent: str) -> str:
    if('Windows' in user_agent):
        return '"Windows"'
    elif('Macintosh' in user_agent):
        return '"Macintosh"'
    elif('Android' in user_agent):
        return '"Android"'
    elif('iPhone' in user_agent):
        return '"iPhone"'
    elif('Linux' in user_agent):
        return '"Linux"'
    else:
        return '"Windows"'
    
def is_mobile(user_agent: str) -> bool:
    if('Android' in user_agent):
        return True
    elif('iPhone' in user_agent):
        return True
    else:
        return False
    
def get_chrome_version(user_agent: str) -> str:
    version_regex = r'Chrome\/(\d+)'
    matches = re.search(version_regex, user_agent)
    first_match = matches.group(0)
    return first_match.lower()
    