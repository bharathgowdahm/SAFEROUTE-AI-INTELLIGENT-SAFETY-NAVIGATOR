from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, DateTime, Text, Integer
from datetime import datetime

class Base(DeclarativeBase): pass

class CommunityReport(Base):
    __tablename__ = "community_reports"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(64))
    lat: Mapped[float] = mapped_column(Float); lon: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(32), default="pending")  # pending/verified/rejected
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class TrustedContact(Base):
    __tablename__ = "trusted_contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(64))
    phone: Mapped[str] = mapped_column(String(32))
    relationship: Mapped[str] = mapped_column(String(64), default="")
