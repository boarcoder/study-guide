from enum import Enum
from pydantic import BaseModel


class Status(Enum):
    INITIALIZING = "INITIALIZING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"
    RESTARTING = "RESTARTING"
    TERMINATING = "TERMINATING"


class SensorData(BaseModel):
    id: int
    frequency: int
    status: Status
    measurement: float
