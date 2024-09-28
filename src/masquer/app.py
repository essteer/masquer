import os
import importlib.util
from .utils.response import get_response
from .utils.validate import validate_args


def setup_logging_if_present():
    """
    Checks whether 'logging_config.py' exists in the parent directory
      if so it imports and sets up the logger
      if not it returns None and logging is not executed
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))

    logging_config_path = os.path.join(
        os.path.dirname(current_dir), "logging_config.py"
    )

    if os.path.isfile(logging_config_path):
        spec = importlib.util.spec_from_file_location(
            "logging_config", logging_config_path
        )
        logging_config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(logging_config)

        logging_config.setup_logging(__name__)
        return logging_config.get_logger(__name__)

    else:
        return None


logger = setup_logging_if_present()


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
        if logger:
            logger.warning(f"Invalid args: [{ua=} {rf=} {hd=}]")
        return {"error": "ua|rf|hd must be blank or boolean"}

    if logger:
        logger.debug(f"Valid args: [{ua=} {rf=} {hd=}]")

    try:
        response = get_response(ua, rf, hd)
        if logger:
            logger.debug(f"Response: [{response}]")

    except Exception as e:
        if logger:
            logger.error(f"Error getting response: {e}")
        return {"error": "Failed to retrieve response"}

    return response
