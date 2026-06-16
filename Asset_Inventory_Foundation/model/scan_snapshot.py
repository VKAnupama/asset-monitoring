from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from database.postgres import Base


class ScanSnapshot(Base):
    __tablename__ = "scan_snapshots"

    id = Column(Integer, primary_key=True, index=True)

    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)

    scanner = Column(String, nullable=False)

    scanned_at = Column(DateTime, default=datetime.utcnow)

    raw_json = Column(Text, nullable=False)

    # Relationship
    asset = relationship("Asset", back_populates="snapshots")
