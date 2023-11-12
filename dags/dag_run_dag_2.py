from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('dag_run_dag_2', description="Dag run dag 2",
          schedule_interval=None, start_date=datetime(2023, 11, 9), catchup=False)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 2", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 2", dag=dag)

task1 >> task2
