import logging
from .utils.response import get_response
from .utils.validate import validate_args

logger = logging.getLogger(__name__)
handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
logger.addHandler(handler)
formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)


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
        return "Error: ua|rf|hd must be blank or boolean"

    logger.debug(f"Valid args: [{ua=} {rf=} {hd=}]")
    response = get_response(ua, rf, hd)
    logger.debug(f"Response: [{response}]")

    return response
