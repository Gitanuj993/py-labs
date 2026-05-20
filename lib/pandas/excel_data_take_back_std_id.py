import pandas as pd

df = pd.read_excel("student_excel_t1.xlsx")
# adding a new column student_id and whose values start from 101
# generate roll_num
std_id_no =[ x for x in range(101,121)]
df['Student_IDs'] = std_id_no

# print(std_id_no)
df.insert(0,'Student_ID',std_id_no)
df.drop(columns='Student_IDs',inplace=True)
# print(df)
print(df.columns)
df.to_excel("student_excel_done_1.xlsx",index=False)