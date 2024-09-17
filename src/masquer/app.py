from src.logging_config import setup_logging, get_logger
from .utils.response import get_response
from .utils.validate import validate_args


setup_logging(__name__)
logger = get_logger(__name__)


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
        logger.warning(f"Invalid args: [{ua=} {rf=} {hd=}]")
        return {"error": "ua|rf|hd must be blank or boolean"}

    logger.debug(f"Valid args: [{ua=} {rf=} {hd=}]")

    try:
        response = get_response(ua, rf, hd)
        logger.debug(f"Response: [{response}]")

    except Exception as e:
        logger.error(f"Error getting response: {e}")
        return {"error": "Failed to retrieve response"}

    return response
