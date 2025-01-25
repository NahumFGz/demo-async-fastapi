from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL
from app.models import Base

# Configuración del motor de base de datos
engine = create_async_engine(DATABASE_URL, echo=True)

# Configuración del sessionmaker
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


# Inicialización de la base de datos
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Función para obtener una sesión
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
