from pymaxapi.models import User
from pydantic import AnyUrl
from typing import Literal

class ChatMember(User):
    description: str | None = None
    avatar_url: AnyUrl
    full_avatar_url: AnyUrl
    last_access_time: int
    is_owner: bool
    is_admin: bool
    join_time: int
    permissions: list[Literal["read_all_messages", "add_remove_members", "add_admins", "change_chat_info", "pin_message", "write", "edit_link"]]