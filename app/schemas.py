from typing import Optional

from pydantic import BaseModel


class SongBase(BaseModel):
    name: str
    artist: str
    year: Optional[int] = None


class SongCreate(SongBase):
    pass


class SongRead(SongBase):
    id: int

    class Config:
        orm_mode = True
