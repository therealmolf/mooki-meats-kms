import db_connect


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

print(db_connect.query_db(sql))


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
"""

col = ['know_id', 'know_name', 'emp_count']
print(db_connect.query_db(sql, df_col=col))


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