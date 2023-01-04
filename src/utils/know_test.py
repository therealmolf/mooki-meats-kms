import pandas as pd


df = pd.read_csv("/home/therealmolf/mooki_meats/src/utils/know_sheet.csv")
df_excel = pd.read_excel("/home/therealmolf/mooki_meats/src/utils/knowledge_data.xlsx")


# print(df_excel.head())
# print(df_excel.columns)
# does not work as intended since prop date uses a randomizer/equation
# thus, we still need to use know_sheet.csv
# print(df_excel['prop_date'])


print(df.head())
print(df.columns)


# for index, row in df.iterrows():
#     for column in df.columns:
#         print(row[column])

print([row for index, row in df.iterrows()])
