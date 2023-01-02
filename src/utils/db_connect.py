import psycopg2
import pandas as pd


HOST = 'localhost'
DATABASE = '172casedb'
USER = 'postgres'
PORT = 5432
PASSWORD = 'rickyrubio17'


def get_db_conn() -> psycopg2.connection:
    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        port=PORT,
        password=PASSWORD
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
