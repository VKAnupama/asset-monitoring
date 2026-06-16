from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from database.postgres import Base

class OpenPort(Base):
    __tablename__ = "open_ports"

    id = Column(Integer, primary_key=True, index=True)

    # Foreign Key → Asset
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)

    port = Column(Integer, nullable=False)

    protocol = Column(String, nullable=False)   # TCP / UDP

    service_name = Column(String, nullable=True)

    banner = Column(Text, nullable=True)

    # Relationship back to Asset
    asset = relationship("Asset", back_populates="open_ports")
