from .utils.response import get_response
from .utils.validate import validate_args


def masq(ua: bool = True, rf: bool = False, hd: bool = False) -> dict:
    """
    Compiles and returns header data via weighted random selection
      - defaults to random user-agent only
      - optionally returns random referer and/or other pre-defined header data

    Parameters
    ----------
    {ua, rf, hd}: bool
        indicates whether useragent | referer | header data requested

    Returns
    -------
    response: dict
        useragent | referer | header data as requested
    """
    valid_args = validate_args(ua, rf, hd)
    if not valid_args:
        return "Error: ua|rf|hd must be blank or boolean"

    response = get_response(ua, rf, hd)

    return response
