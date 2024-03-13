from models import Asset
from sqlalchemy.orm import Session, joinedload

def get_assets(db: Session):
     query_result = db.query(Asset).options(joinedload(Asset.asset_category)).all()
     return query_result