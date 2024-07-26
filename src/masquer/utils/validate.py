def validate_args(ua: bool, rf: bool, hd: bool) -> bool:
    """
    Validates whether arguments are bools
    Returns True if all arguments are bools, else False
    """
    return all(isinstance(arg, bool) for arg in (ua, rf, hd))
