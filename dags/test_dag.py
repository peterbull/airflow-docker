from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,1,1),
}

with DAG('simple_dag',
         default_args=default_args,
         description='A simple test workflow',
         schedule_interval='@daily',
         catchup=False) as dag:

    task1 = EmptyOperator(
        task_id='task1',
    )

    task2 = EmptyOperator(
        task_id='task2',
    )

    task1 >> task2 # task2 depends on task1