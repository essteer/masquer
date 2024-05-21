def validate_params(ua: bool, rf: bool, hd: bool) -> bool:
    """
    Validates whether parameters are bools
    Returns True if all parameters are bools, else False
    """
    return all(isinstance(arg, bool) for arg in (ua, rf, hd))
