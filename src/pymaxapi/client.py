from pymaxapi.config import BASE_URL, TIMEOUT
from pymaxapi._base import _get_pydantic, _auth_headers
import httpx
from pymaxapi.models import BotInfo, Chat
from pymaxapi import _base
import re
import typing_extensions


class MaxAPI:
    def __init__(self, token: str, *, timeout: int = TIMEOUT) -> None:
        self.BASE_URL = BASE_URL
        self.HEADERS = _auth_headers(token)
        self._client = httpx.Client(headers=self.HEADERS, timeout=timeout)

    def close(self) -> None:
        self._client.close()

    # Bots methods
    def me(self) -> BotInfo:
        path = _base._make_url(self.BASE_URL, "me")
        response = self._client.get(path)
        json = _base._parse(response)
        return BotInfo.model_validate(json)

    # Chats methods
    def all_chats(self, count: int = 50, marker: int | None = None) -> list[Chat]:
        if not (1 <= count <= 100):
            raise ValueError("Count должен быть от 1 до 100")

        path = _base._make_url(self.BASE_URL, "chats")
        params = {"count": count, "marker": marker}
        response = self._client.get(path, params=params)
        json = _base._parse(response)
        return [Chat.model_validate(chat) for chat in json.get("chats", [])]

    def get_chat_by_link(self, chat_link: str) -> Chat:
        raise NotImplementedError()

        if re.fullmatch(r"@?[a-zA-Z]+[a-zA-Z0-9-_]*", chat_link) is None:
            raise ValueError(
                r"Chat link должен соответствовать регулярному выражению @?[a-zA-Z]+[a-zA-Z0-9-_]*"
            )

        path = _base._make_url(self.BASE_URL, f"chats/{chat_link}")
        response = self._client.get(path)
        json = _base._parse(response)
        return Chat.model_validate(json)

    def get_chat_by_id(self, chat_id: int) -> Chat:
        path = _base._make_url(self.BASE_URL, f"chats/{chat_id}")
        response = self._client.get(path)
        json = _base._parse(response)
        return json
        return Chat.model_validate(json)

