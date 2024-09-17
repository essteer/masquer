from typing import Union
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..masquer import masq
from ..logging_config import setup_logging, get_logger


setup_logging(__name__)
logger = get_logger(__name__)
router = APIRouter()


@router.get("/masq")
def get_masq(
    ua: Union[bool, None] = True,
    rf: Union[bool, None] = False,
    hd: Union[bool, None] = False,
):
    logger.info(f"Request: [{ua=} {rf=} {hd=}]")
    response = masq(ua, rf, hd)
    logger.info(f"Response: [{response}]")

    return JSONResponse(content=response)
