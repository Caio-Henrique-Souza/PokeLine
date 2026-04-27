from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Adiciona o caminho do projeto ao path para o import funcionar
sys.path.append('/opt/airflow')
from main import run_pipeline

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'dag_poke_pipeline_principal',
    default_args=default_args,
    description='Orquestra o run_pipeline do projeto Pokeline',
    schedule_interval='@daily', 
    catchup=False
) as dag:

    executar_pipeline = PythonOperator(
        task_id='chamada_run_pipeline',
        python_callable=run_pipeline,
        op_kwargs={'extract': True}, # Aqui você passa o parâmetro do seu print
    )