from pymaxapi.models import User, BotCommand
from pydantic import AnyUrl

class BotInfo(User):
    description: str | None = None
    avatar_url: AnyUrl
    full_avatar_url: AnyUrl
    command: list[BotCommand] | None = None