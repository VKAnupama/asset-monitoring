from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from database.postgres import Base


class DnsRecord(Base):
    __tablename__ = "dns_records"

    id = Column(Integer, primary_key=True, index=True)

    # FK → assets table
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)

    # DNS record type (A, AAAA, MX, TXT, CNAME, etc.)
    record_type = Column(String, nullable=False)

    # Value of the record (IP, domain, text, mail server, etc.)
    value = Column(Text, nullable=False)

    # Relationship back to Asset
    asset = relationship("Asset", back_populates="dns_records")
