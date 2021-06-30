from datetime import timedelta, datetime

from automation_and_orchestration.request import BitcoinRequest
from automation_and_orchestration.entry_creator import BitcoinEntryCreator
from automation_and_orchestration.writer import Writer

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'bitcoin_rate',
    default_args=default_args,
    start_date=datetime.now(),
    description='Bitcoin rate',
    schedule_interval='*/30 * * * *',
    catchup=False)

req_node = BitcoinRequest()
creator_node = BitcoinEntryCreator()
writer_node = Writer()



make_request = PythonOperator(
    task_id='make_request',
    python_callable=req_node.execute,
    op_kwargs={'url': 'http://api.coincap.io/v2/rates/bitcoin'},
    dag=dag,
)

create_entry = PythonOperator(
    task_id='create_entry',
    python_callable=lambda **kwargs: creator_node.execute(kwargs["ti"].xcom_pull(task_ids='make_request')),
    dag=dag,
)

write_entry = PythonOperator(
    task_id='write_entry',
    python_callable=lambda **kwargs: writer_node.execute(kwargs["ti"].xcom_pull(task_ids='create_entry')),
    dag=dag,
)

make_request >> create_entry >> write_entry