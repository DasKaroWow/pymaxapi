from pydantic import BaseModel

class BotCommand(BaseModel):
    name: str
    description: str | None = None