import pandas as pd
from google.cloud import storage
import pyarrow.parquet as pq

BUCKET = "s24_bucket_2025"


def upload_to_gcs(bucket, object_name, local_file):
    CREDENTIALS_FILE = "creds.json"
    client = storage.Client.from_service_account_json(CREDENTIALS_FILE)
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


def file_to_gcs(file_name, name, parse_dates):
    df = pd.read_csv(file_name, parse_dates=parse_dates)

    parquet_path = file_name.replace('.csv', '.parquet')
    df.to_parquet(parquet_path,
                  engine='pyarrow',
                  use_deprecated_int96_timestamps=True,
                  coerce_timestamps='ms',
                  allow_truncated_timestamps=False)

    pf = pq.ParquetFile(f"{name}.parquet")
    print(pf.schema)

    upload_to_gcs(BUCKET, f"data/{name}.parquet", parquet_path)
    print(f"Uploaded {name}")


file_to_gcs("currency.csv", name="currency",
            parse_dates=['start_datetime', 'end_datetime'])
file_to_gcs("order_items.csv", name="order_items", parse_dates=[])
file_to_gcs("order_status.csv", name="order_status",
            parse_dates=['paid_at'])
file_to_gcs("orders.csv", name="orders", parse_dates=['paid_at'])
file_to_gcs("products.csv", name="products", parse_dates=[])
file_to_gcs("status.csv", name="status", parse_dates=[])

"""
LOAD DATA TO BIGQUERY ( MANUAL ) TO DO FOR EACH TABLE
1/

CREATE SCHEMA IF NOT EXISTS `s24project.data`

2/

CREATE OR REPLACE EXTERNAL TABLE `s24project.data.external_orders`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://s24_bucket_2025/data/orders.parquet']
);

3/ 

CREATE OR REPLACE TABLE `s24project.data.orders` AS
SELECT * FROM `s24project.data.external_orders`;

"""
