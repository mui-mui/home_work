from sqlalchemy import Column, String, VARCHAR, INTEGER, FLOAT, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

from automation_and_orchestration import metadata

Base = declarative_base(metadata=metadata)


class BitcoinTable(Base):
    __tablename__ = "bitcoin_rate"

    id = Column(VARCHAR(25))
    symbol = Column(VARCHAR(25))
    currency_symbol = Column(VARCHAR(25))
    type = Column(VARCHAR(25))
    rate_usd = Column(FLOAT())
    timestamp = Column(TIMESTAMP(), primary_key=True)

    def __repr__(self):
        return f"<bitcoin_rate {self.id}-{self.timestamp}>"

metadata.create_all()
