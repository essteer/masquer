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
    count: Union[int, None] = 1,
):
    response = [masq(ua, rf, hd)]
    for _ in range(count - 1):
        response.append(masq(ua, rf, hd))
    return JSONResponse(content=response)
