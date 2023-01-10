import psycopg2
import pandas as pd
import os

LOCAL_HOST = "localhost"
LOCAL_DB = "mooki_db"
LOCAL_USER = "postgres"
LOCAL_PASSWORD = "rickyrubio17"


def get_db_conn():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(
        # host=LOCAL_HOST,
        # database=LOCAL_DB,
        # user=LOCAL_USER,
        # port=PORT,
        # password=LOCAL_PASSWORD
        DATABASE_URL,
        # sslmode='require'
    )
    return conn


# TODO: Refactor functions below as there is boilerplate
def modify_db(sql: str, values=None):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    conn.close()


def query_db(sql: str, values=None, df_col=None):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql, values)
    rows = pd.DataFrame(cur.fetchall(), columns=df_col)
    conn.close()
    return rows
