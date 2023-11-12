from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 12),
    'email': ['test@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG('default_args', description="default args",
          default_args=default_args,
          schedule_interval='@hourly', start_date=datetime(2023, 11, 12),
          catchup=False, default_view='graph', tags=['processo', 'tag', 'pipeline'])

task1 = BashOperator(task_id="tsk1", bash_command="sleep 2", dag=dag, retries=3)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 2", dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 2", dag=dag)

task1 >> task2 >> task3
