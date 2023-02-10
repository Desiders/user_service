import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event


@dataclasses.dataclass(frozen=True)
class UserCreated(Event):  # noqa
    user_id: UUID
    username: str
    first_name: str
    last_name: str | None
