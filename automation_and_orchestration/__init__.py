from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

from automation_and_orchestration.system_config import SystemConfig
from automation_and_orchestration.utils.engine import SqlAlchemyEngine

engine = SqlAlchemyEngine(SystemConfig.DATABASE_URI).context
Session = sessionmaker(bind=engine)
metadata = MetaData(engine)
