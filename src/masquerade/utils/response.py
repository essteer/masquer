import json
from .assets import (
    HEADER_DATA,
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
)
from .select import select_data


def get_response(ua: bool, rf: bool, hd: bool) -> str:
    """
    Prepares and returns header data

    Parameters
    ----------
    {ua, rf, hd}: bool
        indicates whether useragent | referer | header data required

    Returns
    -------
    json_header: str
        JSON-formatted header data
    """
    # header data
    if hd:
        header_data = HEADER_DATA
    else:
        header_data = dict()

    # referer
    if rf:
        referer = select_data(REFERERS, REFERER_WEIGHTS)
        header_data["Referer"] = referer

    # user-agent
    if ua:
        useragent = select_data(USERAGENTS, USERAGENT_WEIGHTS)
        header_data["User-Agent"] = useragent

    # serialise response
    json_header = json.dumps(header_data)

    return json_header
