
import db_connect


#TODO: Create test for querying emp and knowledge
#TODO: Create test for FTS with ranking
# TODO: Update Database by adding delete booleans

# TODO: Only select rows that have not been deleted for Employee
# TODO: No option to delete a team
# TODO: For knowledge, show only type, name, prop by, then show only approved and not deleted
# TODO: Make knowledge clickable that goes into a knowledge page


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
# print(db_connect.query_db(sql))


# TODO: Full Text Search for Single Table
search_query = "Improving & hydration"
sql = f"""
        SELECT (know_name, know_desc)
        FROM knowledge
        WHERE to_tsvector('english', know_desc) @@ 
        plainto_tsquery('{search_query}');
"""
# print(db_connect.query_db(sql))


# TODO: Full Text Search for Joined 
# TODO: INNER JOIN the team table, Add Ranking
# Selects team/employee/knowledge + search doc?
search_query = "Protein Demand by Delgado"
search_query = "David Pearson"
search_query = "Spanish Food"

#Shannon returns an empty column because I don't think she is
# associated with any issue
search_query = "Shannon"
sql = f"""
        SELECT
            (
                emp.emp_name,
                emp.team_name,
                knowledge.know_name
            )
        FROM
        emp
        INNER JOIN team
        ON team.team_name = emp.team_name
        INNER JOIN emp_know
        ON emp.emp_id = emp_know.emp_id
        INNER JOIN knowledge
        ON knowledge.know_id = emp_know.know_id
        WHERE to_tsvector(
            'english',
            concat_ws(
                ' ',
                know_desc,
                team_desc,
                emp_desc,
                emp_name,
                emp.team_name,
                degree,
                date_hired,
                know_name
                )) @@
        plainto_tsquery('{search_query}');
"""
print(db_connect.query_db(sql))


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