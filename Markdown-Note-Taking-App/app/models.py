from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    markdown_content = Column(Text, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),server_default=text("now()"))