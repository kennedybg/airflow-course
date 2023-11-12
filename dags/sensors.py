from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.providers.http.sensors.http import HttpSensor
import requests

dag = DAG('http_sensor', description="Http Sensor",
          schedule_interval=None, start_date=datetime(2023, 11, 9), catchup=False, tags=['Sensors'])


def query_api():
    response = requests.get("http://api.publicapis.org/entries")
    print(response.text)


check_api = HttpSensor(task_id="check_api",
                       http_conn_id="my_connection",
                       endpoint="entries",
                       poke_interval=5,
                       timeout=20,
                       dag=dag
                       )

proccess_data = PythonOperator(task_id="proccess_data", python_callable=query_api, dag=dag)

check_api >> proccess_data
