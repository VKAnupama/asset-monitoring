from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from database.postgres import Base


class AssetLog(Base):
    __tablename__ = "asset_logs"

    id = Column(Integer, primary_key=True, index=True)

    # FK → assets table
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)

    # Notification channel (email, slack, webhook, etc.)
    channel = Column(String, nullable=False)

    # status (success, failed, pending)
    status = Column(String, nullable=False)

    # timestamp when message was sent
    sent_at = Column(DateTime, default=datetime.utcnow)

    # Relationship back to Asset
    asset = relationship(
    "Asset",
    back_populates="logs"
    )
    #asset = relationship("Asset", backref="logs")
