from typing import Any
import httpx
from json import JSONDecodeError
from typing import TypeVar
from pydantic import BaseModel
from httpx._types import RequestFiles, QueryParamTypes

# PydanticType = TypeVar("PydanticType", bound=BaseModel)


def _make_url(base_url: str, path: str) -> str:
    return f"{base_url}/{path}"

class APIError(Exception):
    pass

def _parse(response: httpx.Response) -> Any:
    response.raise_for_status()
    content_type = response.headers.get("content-type", "")
    try:
        return response.json()
    except JSONDecodeError as e:
        raise APIError(f"Вернулся не JSON:\nContent-type: {content_type}\nBody: {response.content[:1000]}") from e


def _auth_headers(token: str) -> dict[str, str]:
    return {
        "Content-Type": "application/json",
        "Authorization": token,
    }


def _get_pydantic(
    object_type: type[BaseModel],
    http_client: httpx.Client,
    method: str,
    base_url: str,
    path: str,
    params: QueryParamTypes | None = None,
    json: Any | None = None,
    files: RequestFiles | None = None,
) -> ...:
    url = _make_url(base_url, path)
    response = http_client.request(method, url, params=params, json=json, files=files)
    json = _parse(response)
    return object_type.model_validate(json)


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
