import db_connect
import pandas as pd

# KNOWLEDGE

# How many of each type
sql = """
    SELECT COUNT(*)
    FROM knowledge
    WHERE know_type = 'General'

"""

sql = """
    SELECT COUNT(*)
    FROM knowledge
"""

# print(db_connect.query_db(sql))


# Knowledge with most and least employees knowing it
sql = """

    SELECT t.know_id, k.know_name, t.ce
    FROM
        (SELECT
            know_id,
            COUNT(emp_id) as ce
        FROM
            emp_know
        GROUP BY
            know_id
        ORDER BY
            ce) t
    INNER JOIN
        knowledge k
    on
        k.know_id = t.know_id
    WHERE
        know_delete_ind IS NULL
"""

col = ['know_id', 'know_name', 'emp_count']
print(db_connect.query_db(sql, df_col=col))
print(db_connect.query_db(sql, df_col=col).iloc[-1, 1])


# Get proposal frequency per week
sql = """
    SELECT
        EXTRACT (YEAR FROM prop_date) AS Y,
        EXTRACT (QUARTER FROM prop_date) AS D,
        COUNT(know_id)
    FROM
        knowledge
    GROUP BY
        Y,
        D
    ORDER BY
        Y,
        D

"""
col = ['Year', 'Quarter', 'Count']
print(db_connect.query_db(sql, df_col=col))


# Knowledge Cloud
sql = """
    SELECT know_desc
    FROM
        knowledge
    WHERE
        know_delete_ind IS NULL
"""
col = ['know_desc']
# print(''.join(db_connect.query_db(sql, df_col=col).values.flatten()))


sql = """

    SELECT t.emp_id, e.emp_name, t.ck
    FROM
        (SELECT
            emp_id,
            COUNT(know_id) as ck
        FROM
            emp_know
        GROUP BY
            emp_id
        ORDER BY
            ck) t
    INNER JOIN
        emp e
    on
        e.emp_id = t.emp_id
    WHERE
        emp_delete_ind IS NULL
"""
col = ['emp_id', 'emp_name', 'know_count']
print(db_connect.query_db(sql, df_col=col))


# yearly
sql = """
    SELECT 
        EXTRACT (YEAR FROM date_hired) AS Y,
        COUNT(emp_id)
    FROM
        emp
    GROUP BY
        Y
    ORDER BY
        Y
    DESC
        limit 5
"""


print(db_connect.query_db(sql))