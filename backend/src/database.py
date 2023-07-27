from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(url=settings.database_url, echo=True)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
