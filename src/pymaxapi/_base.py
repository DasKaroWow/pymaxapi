from __future__ import annotations
from typing import Any, Mapping
import httpx
from .config import BASE_URL, TIMEOUT
from json import JSONDecodeError

def _make_url(base_url: str, path: str) -> str:
    return f"{base_url}/{path}"

def _prepare_kwargs(
    *,
    json: Any = None,
    params: Mapping[str, Any] | None = None,
    files: Mapping[str, Any] | None = None,
) -> dict:
    keywords: dict[str, Any] = {}
    if json is not None:
        keywords["json"] = json
    if params:
        keywords["params"] = params
    if files:
        keywords["files"] = files
    return keywords


def _parse(response: httpx.Response) -> dict[str, Any] | list[dict[str, Any]]:
    response.raise_for_status()
    try:
        return response.json()
    except JSONDecodeError:
        raise JSONDecodeError(f"Вернулся не JSON: {response.content}", doc="", pos=0)


def _auth_headers(token: str) -> dict[str, str]:
    return {
        "Content-Type": "application/json",
        "Authorization": token,
    }


# class Client:
#     def __init__(self, token: str, *, timeout: int = TIMEOUT) -> None:
#         self.BASE_URL = BASE_URL
#         self.TOKEN = token
#         self.HEADERS = {
#             "Content-Type": "application/json",
#             "Authorization": self.TOKEN,
#         }
#         self._client = httpx.Client(headers=self.HEADERS, timeout=timeout)

#     def close(self) -> None:
#         self._client.close()



# class AsyncClient:
#     def __init__(
#         self, token: str, *, base_url: str = BASE_URL, timeout: int = TIMEOUT
#     ) -> None:
#         self.base_url = base_url
#         self.timeout = timeout
#         self._c = httpx.AsyncClient(
#             base_url=self.base_url, headers=_auth_headers(token), timeout=timeout
#         )

#     async def aclose(self) -> None:
#         await self._c.aclose()
