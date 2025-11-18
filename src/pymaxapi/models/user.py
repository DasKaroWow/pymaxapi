from pydantic import BaseModel, Field, AnyUrl
from pymaxapi.models.bot_command import BotCommand
from typing import Literal

class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str | None = None
    name: str | None = Field(None, deprecated=True)
    username: str | None = None
    is_bot: bool
    last_activity_time: int

class BotInfo(User):
    description: str | None = None
    avatar_url: AnyUrl
    full_avatar_url: AnyUrl
    command: list[BotCommand] | None = None

class ChatMember(User):
    description: str | None = None
    avatar_url: AnyUrl
    full_avatar_url: AnyUrl
    last_access_time: int
    is_owner: bool
    is_admin: bool
    join_time: int
    permissions: list[Literal["read_all_messages", "add_remove_members", "add_admins", "change_chat_info", "pin_message", "write", "edit_link"]]

class UserWithPhoto(User):
    description: str | None = None
    avatar_url: AnyUrl
    full_avatar_url: AnyUrl