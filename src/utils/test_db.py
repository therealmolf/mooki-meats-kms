
import db_connect

#TODO: Create test for adding, deleting to emp (admin)
#TODO: Create test for proposing, approving, and deleting to knowledge
#TODO: Create test for updating tagging emp_know "who do you think knows this?"

#TODO: Create test for querying emp and knowledge
#TODO: Create test for FTS


# Pattern Matching Query for Single Table
sql = "SELECT (know_name) FROM knowledge WHERE know_desc LIKE '%require%'"
# print(db_connect.query_db(sql))


# TODO: Pattern Matching Query for Joined Table
sql = """
    SELECT
        (
            emp.emp_name,
            emp.team_name,
            knowledge.know_name
        )
    FROM
    emp
    INNER JOIN emp_know
    ON emp.emp_id = emp_know.emp_id
    INNER JOIN knowledge
    ON knowledge.know_id = emp_know.know_id
    WHERE know_name = 'Regulatory Framework'
"""
print(db_connect.query_db(sql))


# TODO: Full Text Search for Single Table
search_query = "Improving & hydration"
sql = f"""
        SELECT (know_name, know_desc)
        FROM knowledge
        WHERE to_tsvector('english', know_desc) @@ 
        plainto_tsquery('{search_query}');
"""

# print(db_connect.query_db(sql))


# TODO: Full Text Search for Joined Table
# TODO: Selects team/employee/knowledge + search doc?


# TODO: Full Text Search with Ranking


# TODO: Adding to Knowledge Table and Tagging emp_know


# TODO: Adding to Emp


# TODO: Updating Approval Status of Khowledge


# TODO: Updating Knowledge Table


# TODO: Deleting Emp


# TODO: Deleting Knowledge





# INSERT INTO emp (emp_name, team_name, role_name, ssn, degree, emp_desc, date_hired) VALUES (
# 'Juan Dela Cruz', 'Hydration', 'Staff Member', '12345678910', 'BS IE', 'Good at X', '2008-11-11');

#INSERT INTO knowledge (know_type, know_name, know_desc, prop_date, prop_by, app_status) VALUES (
#mooki_db(# 'Info', 'TVP', 'Textured vegetable protein (TVP), 
#also known as textured soy protein (TSP), is a high-protein, 
# low-fat product made from soy flour. It is often used as a 
# meat substitute in vegetarian dishes and is known for its 
# ability to absorb flavors well. TVP is often sold in the form of flakes or 
# chunks and must be rehydrated before use. It is a good source of protein 
# for vegetarians and vegans, and it is also used in some non-vegetarian 
# dishes as a way to add protein and reduce the amount of meat needed.',
# '1960-01-01 23:03:20', 'Juan Dela Cruz', 'Approved'); 