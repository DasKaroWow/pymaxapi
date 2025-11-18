from pydantic import BaseModel, AnyUrl
from typing import Literal
from pymaxapi.models.user import User


class Recipient(BaseModel):
    chat_id: int | None = None
    chat_type: Literal["chat"]
    user_id: int | None = None


class PhotoAttachmentPayload(BaseModel):
    photo_id: int
    token: str
    url: AnyUrl

class VideoThumbnail(BaseModel):
    url: AnyUrl

class MediaAttachmentPayload(BaseModel):
    url: AnyUrl
    token: str

class StickerAttachmentPayload(BaseModel):
    url: AnyUrl
    code: str

class ContactAttachmentPayload(BaseModel):
    vcf_info: str | None = None
    max_info: User | None = None

class Keyboard(BaseModel):
    ...

class Attachment(BaseModel):
    type: Literal[
        "image",
        "video",
        "audio",
        "file",
        "sticker",
        "contact",
        "inline_keyboard",
        "share",
        "location",
    ]
    payload: PhotoAttachmentPayload | MediaAttachmentPayload | StickerAttachmentPayload | ContactAttachmentPayload | Keyboard | None

    # video
    thumbnail: VideoThumbnail | None = None
    width: int | None = None
    height: int | None = None
    duration: int | None = None

    # audio
    transcription: str | None = None

    # file
    filename: str | None = None
    size: int | None = None

    # sticker
    # width: int | None = None
    # height: int | None = None

    # share
    title: str | None = None
    description: str | None = None
    image_url: AnyUrl | None = None

    # location
    latitude: float | None = None
    longitude: float | None = None 



class MessageBody(BaseModel):
    mid: str
    seq: int
    text: str | None = None


class Message(BaseModel):
    sender: User
    recipient: Recipient
    timestamp: int
