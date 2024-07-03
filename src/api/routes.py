from typing import Union
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from masquer import masq


router = APIRouter()


@router.get("/masq")
def get_masq(
    ua: Union[bool, None] = True,
    rf: Union[bool, None] = False,
    hd: Union[bool, None] = False,
):
    response = masq(ua, rf, hd)
    return JSONResponse(content=response)
