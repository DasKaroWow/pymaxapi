from pymaxapi.models import User
from pydantic import AnyUrl

class UserWithPhoto(User):
    description: str | None = None
    avatar_url: AnyUrl
    full_avatar_url: AnyUrl