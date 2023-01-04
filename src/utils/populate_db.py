# pip install Faker
import db_connect
import pandas as pd

#TODO: Populate team TABLE and knowledge TABLE
#TODO: Create db_test basic
#TODO: Create custom knowledge and employee profile using Faker
#TODO: Generate fake data\
#TODO: Update Database by adding delete booleans
#TODO: Place in database via refactored db_connect
#TODO: Populate emp_know TABLE and team TABLE using the data in database
#TODO: Create FTS test
#TODO: Create Update test
# for me not to have to separately populate, need to seed random data


TEAM_DATA = [
    ("TVP",
        "In charge of receiving Textured Vegetable Protein"),
    ("Hydration",
        "In charge of combining heated water, broth, and or/fats to TVP"),
    ("ESLP",
        "Stands for Extended Shelf-Life Processes. In charge of prolonging \
            shelf life"),
    ("Cooking",
        "In charge of using various thermal process such as frying and \
            boiling"),
    ("Coating",
        "In charge of adding adhesive components and desered exterior \
            coatings"),
    ("Cooling",
        "In charge of refrigeration, freezing, or a combination of these \
            methods"),
    ("Packaging",
        "In charge of storing and packaging based on requirements and \
            customer uses"),
]


def populate_team():
    # if team has data then delete
    TABLE = 'team'
    for team in TEAM_DATA:
        team_name = team[0]
        team_desc = team[1]

        sql = f"""INSERT INTO {TABLE}
                (
                    team_name,
                    team_desc
                )
                VALUES
                (
                    '{team_name}',
                    '{team_desc}'
                    )"""
       
        db_connect.modify_db(sql)

    print("Just finished!")


#TODO: Fix know sheet delimiters since the text body has commas
def populate_knowledge():

    TABLE = 'knowledge'
    df = pd.read_csv("/home/therealmolf/mooki_meats/src/utils/know_sheet.csv")

    for index, row in df.iterrows():

        # remove quotations from knowledge text
        know_text = row[df.columns[2]].replace("\'", "")

        sql = f"""INSERT INTO {TABLE}
                (
                    {', '.join(df.columns)}
                )
                VALUES
                (
                    '{row[df.columns[0]]}',
                    '{row[df.columns[1]]}',
                    '{know_text}',
                    '{row[df.columns[3]]}',
                    '{row[df.columns[4]]}',
                    '{row[df.columns[5]]}'
                    )"""
        db_connect.modify_db(sql)
    
    print("Just Finished Populating Knowledge")


def populate_emp():
    # faker
    pass


def populate_emp_know():
    pass


# populate_team()
populate_knowledge()

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