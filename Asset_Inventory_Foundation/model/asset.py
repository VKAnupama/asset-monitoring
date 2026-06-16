from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship   
from database.postgres import Base
from datetime import datetime


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)

    domain = Column(String, nullable=False)

    ip_address = Column(String, nullable=False)

    asset_type = Column(String, nullable=False)

    first_scan = Column(DateTime, default=datetime.utcnow)
    # NEW: Last time asset was observed
    last_seen = Column(DateTime, default=datetime.utcnow)

    # NEW: Internal / External asset flags
    is_internal = Column(Boolean, default=False)

    is_external = Column(Boolean, default=True)

    # 🔗 Relationship with Vulnerability
    vulnerabilities = relationship(
        "Vulnerability",
        back_populates="asset",
        cascade="all, delete-orphan"
    )
    # 🔗 Relationship with Open Ports
    open_ports = relationship(
        "OpenPort",
        back_populates="asset",
        cascade="all, delete-orphan"
    )

    # 🔗 Relationship with dns record
    dns_records = relationship(
        "DnsRecord",
        back_populates="asset",
        cascade="all, delete-orphan"
    )


    # 🔗 Relationship with AssetChange
    changes = relationship(
        "AssetChange",
        back_populates="asset",
        cascade="all, delete-orphan"
    )
    # 🔗 Relationship with AssetLog
    logs = relationship(
        "AssetLog",
        back_populates="asset",      #   backref="asset",
        cascade="all, delete-orphan"
    )
    # 🔗 Relationship with scan snapshot
    snapshots = relationship(
        "ScanSnapshot",
        back_populates="asset",
        cascade="all, delete-orphan"
    )
