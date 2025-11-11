from pydantic import BaseModel, Field

class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str | None = None
    name: str | None = Field(None, deprecated=True)
    username: str | None = None
    is_bot: bool
    last_activity_time: int
