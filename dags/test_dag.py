from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello from task1")

def print_goodbye():
    print("Goodbye from task2")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,1,1),
}

with DAG('simple_dag',
         default_args=default_args,
         description='A simple test workflow',
         schedule_interval='@daily',
         catchup=False) as dag:

    task1 = PythonOperator(
        task_id='task1',
        python_callable=print_hello,
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=print_goodbye,
    )

    task1 >> task2 # task2 depends on task1