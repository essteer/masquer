from utils.response import get_response
from utils.validate import validate_params


def masq(ua: bool=True, rf: bool=False, hd: bool=False) -> str:
    """
    Compiles and returns header data via weighted random selection
      - defaults to random user-agent only
      - optionally returns random referer and/or other pre-defined header data
    
    Parameters
    ----------
    {ua, rf, hd}: bool
        indicates whether useragent | referer | header data required
    
    Returns
    -------
    response: str
        JSON-formatted header data
    """
    valid_params = validate_params(ua, rf, hd)
    
    if not valid_params:
        return "TypeError: non-boolean parameters supplied for ua | rf | hd"
    
    response = get_response(ua, rf, hd)
        
    return response

