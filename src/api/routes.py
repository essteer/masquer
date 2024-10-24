from typing import Union
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..masquer import masq
from ..logging_config import setup_logging, get_logger


setup_logging(__name__)
logger = get_logger(__name__)
router = APIRouter()

MAX_COUNT = 250
MIN_COUNT = 1


@router.get("/masq", include_in_schema=False)  # maintain for backwards compatibility
@router.get("/api/v0/masq", summary="Get a single object")
def get_masq_v0(
    ua: Union[bool, None] = True,
    rf: Union[bool, None] = False,
    hd: Union[bool, None] = False,
):
    logger.info(f"Request: [{ua=} {rf=} {hd=}]")
    response = masq(ua, rf, hd)
    logger.debug(f"Response: {response}")

    return JSONResponse(content=response)


@router.get("/api/v1/masq", summary="Get an array of objects")
def get_masq(
    ua: Union[bool, None] = True,
    rf: Union[bool, None] = False,
    hd: Union[bool, None] = False,
    count: Union[int, None] = 1,
):
    logger.info(f"Request: [{ua=} {rf=} {hd=} {count=}]")
    if count >= MAX_COUNT:
        count = MAX_COUNT
    if count <= MIN_COUNT:
        count = MIN_COUNT
    response = [masq(ua, rf, hd) for _ in range(count)]
    logger.debug(f"Response: {response}")

    return JSONResponse(content=response)
