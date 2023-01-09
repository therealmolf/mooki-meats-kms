import psycopg2
import pandas as pd
import os


# HOST = 'localhost'
# DATABASE = 'mooki_db'
# USER = 'postgres'
# PORT = 5432
# PASSWORD = 'rickyrubio17'


def get_db_conn():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(
        DATABASE_URL,
        sslmode='require'
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
