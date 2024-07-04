from pydantic import BaseModel


class StatusCountResponse(BaseModel):
    _id: int
    count: int
