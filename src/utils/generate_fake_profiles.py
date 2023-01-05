import random
from faker import Faker
import pandas as pd


COLUMNS = [
    "emp_name",
    "team_name",
    "role_name",
    "ssn",
    "degree",
    "emp_desc",
    "date_hired"
]

JOBS = [
        "Staff",
        "Assistant",
        "Engineer",
        "Developer",
        "Technician"
]

DEG = [
    "BS Industrial Engineering",
    "BS Economics",
    "BS Food Science",
    "BS Management",
    "BS Computer Science"
]

TEAM = [
    "TVP",
    "Hydration",
    "ESLP",
    "Cooking",
    "Coating",
    "Cooling",
    "Packaging",
]


fake = Faker()
fake.random.seed(1234)


def generate_fake_profiles(num=10):

    df = pd.DataFrame(columns=COLUMNS)

    for row in range(num):
        row_list = []

        row_list.append(fake.name())
        row_list.append(random.choice(TEAM))
        row_list.append(random.choice(JOBS))
        row_list.append('{:03}'.format(random.randrange(1, 10**11)))
        row_list.append(random.choice(DEG))
        row_list.append(fake.text())
        row_list.append(fake.date())

        df.loc[len(df)] = row_list

    return df


generate_fake_profiles(50).to_csv("/home/therealmolf/mooki_meats/src/utils/\
    emp_sheet.csv", index=False)

# INSERT INTO emp (emp_name, team_name, role_name, ssn, degree,
# emp_desc, date_hired) VALUES (
# 'Juan Dela Cruz', 'Hydration', 'Staff Member', '12345678910',
# 'BS IE', 'Good at X', '2008-11-11');
