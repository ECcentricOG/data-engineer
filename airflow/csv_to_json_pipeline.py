import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

import pandas as pd

def csv_to_json():
    df = pd.read_csv("data/data.csv")
    for _, row in df.iterrows():
        print(row['name'])
    df.to_json("data/csv_to_json.json", orient="records")

args = {
    'owner': 'ECcentriOG',
    'start_date': dt.datetime(2026, 3, 3),
    'retries': 2,
    'retry_delay': dt.timedelta(minutes=3)
}

with DAG('MyCSVDAG',
         default_args = args,
         schedule = timedelta(minutes=3),
         # '0 * * * *'
         ) as dag:
    print_starting = BashOperator(task_id = 'starting', 
                                  bash_command = 'echo "Started converting csv to json"')
    CSVJson = PythonOperator(task_id = 'convert_csv_to_json', python_callable = csv_to_json)

    print_starting >> CSVJson
