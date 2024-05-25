from .assets import (
    HEADER_DATA,
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
)
from .select import select_data


def get_response(ua: bool, rf: bool, hd: bool) -> dict:
    """
    Prepares and returns header data

    Parameters
    ----------
    {ua, rf, hd}: bool
        indicates whether useragent | referer | header data required

    Returns
    -------
    response_data: dict
        useragent | referer | header data as requested
    """
    # header data
    if hd:
        response_data = HEADER_DATA
    else:
        response_data = dict()

    # referer
    if rf:
        referer = select_data(REFERERS, REFERER_WEIGHTS)
        response_data["Referer"] = referer

    # user-agent
    if ua:
        useragent = select_data(USERAGENTS, USERAGENT_WEIGHTS)
        response_data["User-Agent"] = useragent

    return response_data
