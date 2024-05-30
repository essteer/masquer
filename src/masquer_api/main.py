from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from masquer import masq
from masquer.__about__ import __version__


DESCRIPTION = """
Use `masquer API` to obtain any combination of a random user-agent, referer or header data template, then use this with a library like [`requests`](https://github.com/psf/requests) to control the session data you send to other services.

The user-agent data is drawn from [this list](https://www.useragents.me/) of the most common desktop user-agents, and referer data is taken from [this list](https://gs.statcounter.com/search-engine-market-share/desktop/worldwide) of search engines with the largest global market share.

Weighted random selections are made from those lists to approximate authentic header data patterns.

A basic header template with common attributes — including the recommended [`"Upgrade-Insecure-Requests": "1"`](https://stackoverflow.com/questions/31950470/what-is-the-upgrade-insecure-requests-http-header/32003517#32003517) — is also provided and defaults to the most common referer and user-agent data from the above lists.
"""

VERSION = __version__

app = FastAPI(
    title="Masquer API",
    summary="A tool to generate random user-agent and referer data for GET requests.",
    description=DESCRIPTION,
    version=VERSION,
    license_info={
        "name": "MIT License",
        "url": "https://github.com/essteer/masquer/blob/main/LICENSE",
    },
)


@app.get("/masq")
def get_masq(
    ua: Union[bool, None] = True,
    rf: Union[bool, None] = False,
    hd: Union[bool, None] = False,
):
    response = masq(ua, rf, hd)
    return JSONResponse(content=response)
