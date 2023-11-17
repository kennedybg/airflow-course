from airflow import DAG
from datetime import datetime
from big_data_operator import BigDataOperator

dag = DAG('big_data', description="Big Data",
          schedule_interval=None, start_date=datetime(2023, 11, 9), catchup=False, tags=['big_data'])

big_data = BigDataOperator(
    task_id="big_data",
    path_to_csv_file="/opt/airflow/data/Churn.csv",
    path_to_save_file="/opt/airflow/data/Churn.json",
    file_type="json",
    dag=dag
)

big_data
