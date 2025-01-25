from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db import get_session
from app.models import Song
from app.schemas import SongCreate, SongRead

router = APIRouter()


@router.get("/ping")
async def pong():
    return {"ping": "pong!"}


@router.get("/songs", response_model=list[SongRead])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    return result.scalars().all()


@router.post("/songs", response_model=SongRead)
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    new_song = Song(**song.dict())
    session.add(new_song)
    await session.commit()
    await session.refresh(new_song)
    return new_song
