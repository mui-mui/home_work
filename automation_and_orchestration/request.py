from abc import abstractmethod

from automation_and_orchestration.airflow_node import IAirflowNode
import requests


class Request(IAirflowNode):

    def execute(self, url):
        return self._parse_func(requests.get(url).json())

    @abstractmethod
    def _parse_func(self, *args, **kwargs):
        pass


class BitcoinRequest(Request):

    def _parse_func(self, data):
        data_ = data['data']
        data_['timestamp'] = data['timestamp']
        return data_


if __name__ == '__main__':
    r = BitcoinRequest()
    print(r.execute("http://api.coincap.io/v2/rates/bitcoin"))
    