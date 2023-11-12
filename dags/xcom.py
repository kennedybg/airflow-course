from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

dag = DAG('xcom_1', description="xcom 1",
          schedule_interval=None, start_date=datetime(2023, 11, 9), catchup=False)


def task_write(**kwargs):
    kwargs['ti'].xcom_push(key='valor_xcom_1', value=10200)

def task_read(**kwargs):
    valor = kwargs['ti'].xcom_pull(key='valor_xcom_1')
    print(f"valor recuperado : {valor}")

task1 = PythonOperator(task_id="tsk1", python_callable=task_write, dag=dag)
task2 = PythonOperator(task_id="tsk2", python_callable=task_read, dag=dag)

task1 >> task2
