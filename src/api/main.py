import sys
import os
from fastapi import FastAPI
from ..masquer.__about__ import __version__
from ..logging_config import setup_logging, get_logger
from .routes import router


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

setup_logging(__name__)
logger = get_logger(__name__)

DESCRIPTION = """
Use `masquer` to obtain any combination of a random user-agent, referer or header data template, then use this with a library like [`requests`](https://github.com/psf/requests) to control the session data you send to other services.

The user-agent data is drawn from [this list](https://www.useragents.me/) of the most common desktop user-agents, and referer data is taken from [this list](https://gs.statcounter.com/search-engine-market-share/desktop/worldwide) of search engines with the largest global market share.

Weighted random selections are made from those lists to approximate authentic header data patterns.

A basic header template with common attributes — like [`"Upgrade-Insecure-Requests": "1"`](https://stackoverflow.com/questions/31950470/what-is-the-upgrade-insecure-requests-http-header/32003517#32003517) — is also provided and defaults to the most common referer and user-agent data from the above lists.

## Requests

The code examples below illustrate methods for making API calls in different languages.

### cURL

```console
$ curl -X GET 'https://masquer.fly.dev/masq?ua=true&rf=false&hd=false' -H 'accept: application/json'
```

### JavaScript (using `fetch`)

```javascript
fetch('https://masquer.fly.dev/masq?ua=true&rf=false&hd=false')
  .then(response => response.json())
  .then(data => console.log(data))
```

### Python (using `requests`)

```python
import requests
response = requests.get("https://masquer.fly.dev/masq", params={"ua": True, "rf": False, "hd": False})
print(response.json())
```
"""

SUMMARY = "A tool to generate random user-agent and referer data for HTTP requests."


def get_app() -> FastAPI:
    """
    Create a FastAPI app with the specified attributes
    """
    try:
        app = FastAPI(
            title="Masquer API",
            summary=SUMMARY,
            description=DESCRIPTION,
            version=__version__,
            license_info={
                "name": "MIT License",
                "url": "https://github.com/essteer/masquer/blob/main/LICENSE",
            },
        )
        app.include_router(router)
        logger.info("FastAPI app init OK")

        return app

    except Exception as e:
        logger.error(f"FastAPI app init error: {e}")


app = get_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
