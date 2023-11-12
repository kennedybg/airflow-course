from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.models import Variable

dag = DAG('variaveis_1', description="Variaveis 1",
          schedule_interval=None, start_date=datetime(2023, 11, 9), catchup=False)

def print_variable(**context):
    minha_var = Variable.get('minhavar')
    print(f"O valor da variavel é : {minha_var}")

task1 = PythonOperator(task_id="tsk1", python_callable=print_variable, dag=dag)

task1