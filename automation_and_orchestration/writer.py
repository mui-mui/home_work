from sqlalchemy.exc import SQLAlchemyError

from automation_and_orchestration import Session
from automation_and_orchestration.airflow_node import IAirflowNode
from automation_and_orchestration.models import Base


class Writer(IAirflowNode):
    def __init__(self):
        self.session = Session()

    def execute(self, entry: Base):
        try:
            self.session.add(entry)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Ошибка вставки записи в таблицу {entry.__tablename__} ({entry.__repr__()}) - {e}")
            raise SQLAlchemyError()