from .assets import (
    HEADER_DATA,
    REFERERS,
    REFERER_WEIGHTS,
    USERAGENTS,
    USERAGENT_WEIGHTS,
    SEC_CH_UA
)
from .select import select_ch_ua, select_data


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
        if "Safari/537" in useragent:
            sec_dict = select_ch_ua(useragent, SEC_CH_UA)
            if(sec_dict):
                response_data['Sec-CH-UA'] = sec_dict['sec-ch-ua']
                response_data['Sec-CH-UA-Mobile'] = sec_dict['sec-ch-ua-mobile']
                response_data['Sec-CH-UA-Platform'] = sec_dict['sec-ch-ua-platform']

    return response_data
