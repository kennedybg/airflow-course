from airflow import DAG
from airflow import Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

mydataset = Dataset("/opt/airflow/data/Churn_new.csv")

dag = DAG('consumer', description="Consumer",
          schedule=[mydataset], start_date=datetime(2023, 11, 9), catchup=False,
          tags=['datasets'])


def my_file():
    dataset = pd.read_csv("/opt/airflow/data/Churn_new.csv", sep=";")
    dataset.to_csv("/opt/airflow/data/Churn_new_2.csv")


t1 = PythonOperator(task_id="t1", python_callable=my_file,
                    dag=dag, provide_context=True)

t1
