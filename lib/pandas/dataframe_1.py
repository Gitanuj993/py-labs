import pandas as pd
employee_data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],

    "Name": [
        "Aarav Sharma",
        "Priya Verma",
        "Rahul Mehta",
        "Sneha Patil",
        "Vikram Singh",
        "Neha Joshi",
        "Karan Malhotra",
        "Anjali Desai"
    ],

    "Department": [
        "IT",
        "HR",
        "Finance",
        "Marketing",
        "Sales",
        "IT",
        "Operations",
        "Finance"
    ],

    "Age": [25, 29, 35, 28, 32, 26, 40, 31],

    "Salary": [45000, 52000, 68000, 48000, 75000, 47000, 82000, 61000],

    "Experience_Years": [2, 4, 10, 3, 8, 2, 15, 6],

    "City": [
        "Indore",
        "Bhopal",
        "Mumbai",
        "Pune",
        "Delhi",
        "Hyderabad",
        "Bangalore",
        "Ahmedabad"
    ],

    "Performance_Rating": [4.2, 4.7, 4.5, 3.9, 4.8, 4.1, 4.9, 4.4],

    "Remote_Work": [True, False, True, False, True, True, False, False]
}
employee_df = pd.DataFrame(employee_data)
pd.set_option("display.width",None)
print(employee_df)