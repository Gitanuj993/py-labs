import pandas as pd
data = [
    {
        "Employee_ID": 101,
        "Name": "Aarav Sharma",
        "Department": "IT",
        "Age": 25,
        "Salary": 45000,
        "Experience_Years": 2,
        "City": "Indore",
        "Performance_Rating": 4.2,
        "Remote_Work": true
    },
    {
        "Employee_ID": 102,
        "Name": "Priya Verma",
        "Department": "HR",
        "Age": 29,
        "Salary": 52000,
        "Experience_Years": 4,
        "City": "Bhopal",
        "Performance_Rating": 4.7,
        "Remote_Work": false
    },
    {
        "Employee_ID": 103,
        "Name": "Rahul Mehta",
        "Department": "Finance",
        "Age": 35,
        "Salary": 68000,
        "Experience_Years": 10,
        "City": "Mumbai",
        "Performance_Rating": 4.5,
        "Remote_Work": true
    },
    {
        "Employee_ID": 104,
        "Name": "Sneha Patil",
        "Department": "Marketing",
        "Age": 28,
        "Salary": 48000,
        "Experience_Years": 3,
        "City": "Pune",
        "Performance_Rating": 3.9,
        "Remote_Work": false
    },
    {
        "Employee_ID": 105,
        "Name": "Vikram Singh",
        "Department": "Sales",
        "Age": 32,
        "Salary": 75000,
        "Experience_Years": 8,
        "City": "Delhi",
        "Performance_Rating": 4.8,
        "Remote_Work": true
    },
    {
        "Employee_ID": 106,
        "Name": "Neha Joshi",
        "Department": "IT",
        "Age": 26,
        "Salary": 47000,
        "Experience_Years": 2,
        "City": "Hyderabad",
        "Performance_Rating": 4.1,
        "Remote_Work": true
    },
    {
        "Employee_ID": 107,
        "Name": "Karan Malhotra",
        "Department": "Operations",
        "Age": 40,
        "Salary": 82000,
        "Experience_Years": 15,
        "City": "Bangalore",
        "Performance_Rating": 4.9,
        "Remote_Work": false
    },
    {
        "Employee_ID": 108,
        "Name": "Anjali Desai",
        "Department": "Finance",
        "Age": 31,
        "Salary": 61000,
        "Experience_Years": 6,
        "City": "Ahmedabad",
        "Performance_Rating": 4.4,
        "Remote_Work": False
    }
]

json_df = pd.read_json(data)
print(json_df)