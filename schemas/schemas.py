from pydantic import BaseModel


class GetValues(BaseModel):
    x: int
    y: int
    operator: str
