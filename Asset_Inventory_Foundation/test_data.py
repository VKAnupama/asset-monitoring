from datetime import datetime

from database.postgres import engine
from sqlalchemy.orm import sessionmaker

from model.asset import Asset
from model.vulnerability import Vulnerability
from model.open_port import OpenPort
from model.dns_record import DnsRecord
from model.scan_snapshot import ScanSnapshot
from model.asset_change import AssetChange
from model.asset_log import AssetLog


SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


# Create Asset
asset = Asset(
    domain="example.com",
    ip_address="192.168.1.10",
    asset_type="server",
    first_scan=datetime.utcnow(),
    last_seen=datetime.utcnow(),
    is_internal=True,
    is_external=False
)

session.add(asset)
session.commit()
session.refresh(asset)

print(f"Asset Created: {asset.id}")


# Vulnerability
vuln = Vulnerability(
    asset_id=asset.id,
    cve_id="CVE-2025-1234",
    severity="High",
    cvss_score=8.5,
    template_id="temp-001",
    remediation="Update software"
)

session.add(vuln)


# Open Port
port = OpenPort(
    asset_id=asset.id,
    port=22,
    protocol="TCP",
    service_name="SSH",
    banner="OpenSSH 9.0"
)

session.add(port)


# DNS Record
dns = DnsRecord(
    asset_id=asset.id,
    record_type="A",
    value="192.168.1.10"
)

session.add(dns)


# Scan Snapshot
snapshot = ScanSnapshot(
    asset_id=asset.id,
    scanner="Nmap",
    raw_json='{"ports":[22,80,443]}'
)

session.add(snapshot)


# Asset Change
change = AssetChange(
    asset_id=asset.id,
    change_type="Port Added",
    old_value="80",
    new_value="443",
    risk_score=7.5
)

session.add(change)


# Asset Log
log = AssetLog(
    asset_id=asset.id,
    channel="email",
    status="success"
)

session.add(log)

session.commit()

print("All test data inserted successfully!")

session.close()
