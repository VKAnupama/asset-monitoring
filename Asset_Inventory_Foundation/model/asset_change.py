from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database.postgres import Base


class AssetChange(Base):
    __tablename__ = "asset_changes"

    id = Column(Integer, primary_key=True, index=True)

    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)

    change_type = Column(String, nullable=False)

    old_value = Column(Text, nullable=True)

    new_value = Column(Text, nullable=True)

    risk_score = Column(Float, nullable=True)

    detected_at = Column(DateTime, default=datetime.utcnow)

    # Relationship
    asset = relationship(
    "Asset",
    back_populates="changes"
    )
    #asset = relationship("Asset", backref="changes")
