from pydantic import BaseModel, AnyUrl
from typing import Literal
from pymaxapi.models.user import UserWithPhoto
from pymaxapi.models.message import Message

class Image(BaseModel):
    url: AnyUrl

class Chat(BaseModel):
    chat_id: int
    type: Literal["chat"]
    status: Literal["active", "removed", "left", "closed"]
    title: str | None = None
    icon: Image | None = None
    last_event_time: int
    participants_count: int
    owner_id: int | None = None
    participants: dict[str, int] | None = None
    is_public: bool
    link: AnyUrl | None = None
    description: str | None = None
    dialog_with_user: UserWithPhoto | None = None
    chat_message_id: str | None = None
    inned_message: Message | None = None