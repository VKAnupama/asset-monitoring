from database.postgres import engine, Base

# Import ALL models so SQLAlchemy registers them
from model.asset import Asset
from model.vulnerability import Vulnerability
from model.open_port import OpenPort
from model.dns_record import DnsRecord
from model.scan_snapshot import ScanSnapshot
from model.asset_change import AssetChange
from model.asset_log import AssetLog

def init_db():
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully!")


if __name__ == "__main__":
    init_db()
