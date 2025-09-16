# Document the steps to create an Apache AirFlow DAG that accepts a url using llama-index, extracts the text from the html, converts the unstructured text to a pydantic class and then write it to a Postgres vector database

## Steps to Create an Apache AirFlow DAG

1. **Install Required Packages**:
    ```bash
    pip install apache-airflow llama-index pydantic psycopg2
    ```

2. **Create the DAG File**:
    ```python
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import requests
    from llama_index import extract_text
    from pydantic import BaseModel
    import psycopg2

    class ExtractedData(BaseModel):
        title: str
        content: str

    def fetch_url_content(url):
        response = requests.get(url)
        return response.text

    def process_content(html_content):
        text = extract_text(html_content)
        data = ExtractedData(title="Sample Title", content=text)
        return data

    def write_to_postgres(data):
        conn = psycopg2.connect("dbname=test user=postgres password=secret")
        cur = conn.cursor()
        cur.execute("INSERT INTO vector_table (title, content) VALUES (%s, %s)", (data.title, data.content))
        conn.commit()
        cur.close()
        conn.close()

    default_args = {
        'owner': 'airflow',
        'start_date': datetime(2023, 1, 1),
        'retries': 1,
    }

    with DAG('example_dag', default_args=default_args, schedule_interval='@daily') as dag:
        fetch_task = PythonOperator(
            task_id='fetch_url_content',
            python_callable=fetch_url_content,
            op_args=['http://example.com'],
        )

        process_task = PythonOperator(
            task_id='process_content',
            python_callable=process_content,
            provide_context=True,
        )

        write_task = PythonOperator(
            task_id='write_to_postgres',
            python_callable=write_to_postgres,
            provide_context=True,
        )

        fetch_task >> process_task >> write_task
    ```

3. **Deploy the DAG**:
    - Save the above code in a file named `example_dag.py` and place it in your Airflow DAGs directory.

4. **Start Airflow**:
    - Initialize the database:
        ```bash
        airflow db init
        ```
    - Start the web server:
        ```bash
        airflow webserver --port 8080
        ```
    - Start the scheduler:
        ```bash
        airflow scheduler
        ```

5. **Monitor the DAG**:
    - Open the Airflow web UI at `http://localhost:8080` and trigger the DAG manually or wait for the scheduled interval.