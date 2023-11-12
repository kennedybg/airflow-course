from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from datetime import datetime
import random

dag = DAG('branch_test', description="Branch test",
          schedule_interval=None, start_date=datetime(2023, 11, 9), catchup=False)


def random_num():
    return random.randint(1, 100)


generate_random_number_task = PythonOperator(
    task_id="gen_number_task", python_callable=random_num, dag=dag)


def evaluate_rand_num(**context):
    number = context['task_instance'].xcom_pull(task_ids='gen_number_task')
    if number % 2 == 0:
        return 'par_task'
    else:
        return 'impar_task'


branch_task = BranchPythonOperator(
    task_id="branch_task",
    python_callable=evaluate_rand_num,
    provide_context=True,
    dag=dag)

par_task = BashOperator(task_id="par_task", bash_command='echo "Número par"',
                        dag=dag)

impar_task = BashOperator(task_id="impar_task", bash_command='echo "Número ímpar"',
                          dag=dag)

generate_random_number_task >> branch_task
branch_task >> par_task
branch_task >> impar_task
