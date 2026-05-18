import pandas as pd

pd.set_option("display.width",None)
excel_df  = pd.read_excel("./files/employee_data.xlsx")
print(excel_df)