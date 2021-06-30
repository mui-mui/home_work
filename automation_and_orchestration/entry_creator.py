from abc import abstractmethod

from automation_and_orchestration.airflow_node import IAirflowNode
from automation_and_orchestration.models import BitcoinTable


class EntryCreator(IAirflowNode):
    def execute(self, data):
        return self._create_table_entry(data)

    @abstractmethod
    def _create_table_entry(self, data):
        pass


class BitcoinEntryCreator(EntryCreator):
    def _create_table_entry(self, data):
        entry = BitcoinTable()
        entry.id = data["id"]
        entry.type = data["type"]
        entry.symbol = data["symbol"]
        entry.currency_symbol = data["currency_symbol"]
        entry.rate_usd = data["rate_usd"]
        entry.timestamp = data["timestamp"]
        return entry
