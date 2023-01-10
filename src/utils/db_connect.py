import psycopg2
import pandas as pd
import os


HOST = 'ec2-3-209-124-113.compute-1.amazonaws.com'
DATABASE = 'd53gumo0i7ad3h'
USER = 'ethiewwcdjsojh'
PORT = 5432
PASSWORD = '0c09d8a125a30a74980999d9d33943f7ac3d845d57684327c7378bc53b924ad0'


def get_db_conn():
    # DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        port=PORT,
        password=PASSWORD
        # DATABASE_URL,
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
