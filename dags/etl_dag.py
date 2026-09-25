from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import src.for_sql as for_sql

default_args = {
    'owner': 'fedos',
    'depends_on_past': False,
    'start_date': datetime(2026, 9, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'data_pipeline',
    default_args=default_args,
    description='Simple ETL pipeline :)',
    schedule_interval='0 */1 * * *',
    catchup=False,
    tags=['currency', 'crypto', 'example', 'Fedos'],
) as dag:

    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=for_sql.insert_info,
    )

    etl_task
