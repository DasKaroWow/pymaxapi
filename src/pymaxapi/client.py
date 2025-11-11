from pymaxapi.config import BASE_URL, TIMEOUT
from pymaxapi import _base
import httpx
from pymaxapi.models import BotInfo

class MaxAPI:
    def __init__(self, token: str, *, timeout: int = TIMEOUT) -> None:
        self.BASE_URL = BASE_URL
        self.HEADERS = _base._auth_headers(token)
        self._client = httpx.Client(headers=self.HEADERS, timeout=timeout)

    def close(self) -> None:
        self._client.close()

    def me(self) -> BotInfo:
        path = _base._make_url(self.BASE_URL, "me")
        response = self._client.get(path)
        json = _base._parse(response)

        return BotInfo.model_validate(json)



