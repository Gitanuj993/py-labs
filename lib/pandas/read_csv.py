import pandas as pd

file = pd.read_csv("student_data_3.csv")
# df = file.iloc[0:1]
df = file.iloc[: , 1:]
df.to_excel("student_excel_t1.xlsx" , index = False)
print(df)
