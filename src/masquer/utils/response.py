from .assets import (
    HEADER_DATA,
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
)
from .select import select_data


def get_response(
    useragent_requested: bool, referer_requested: bool, header_requested: bool
) -> dict:
    """
    Prepares and returns header data

    Parameters
    ----------
    {useragent_requested, referer_requested, header_requested}: bool
        indicates whether useragent | referer | header data required

    Returns
    -------
    response_data: dict
        useragent | referer | header data as requested
    """
    response_data = dict()

    if header_requested:
        response_data = dict(HEADER_DATA)

    if referer_requested:
        referer = select_data(REFERERS, REFERER_WEIGHTS)
        response_data["Referer"] = referer

    if useragent_requested:
        useragent = select_data(USERAGENTS, USERAGENT_WEIGHTS)
        response_data["User-Agent"] = useragent

    return response_data
