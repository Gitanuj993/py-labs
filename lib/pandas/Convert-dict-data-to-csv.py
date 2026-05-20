import pandas as pd

students = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 116, 117, 118, 119, 120],

    "Name": [
        "Aarav Sharma", "Priya Verma", "Rahul Mehta", "Sneha Patel",
        "Vikram Singh", "Ananya Gupta", "Rohan Das", "Kavya Nair",
        "Arjun Rao", "Neha Joshi", "Ishaan Kapoor", "Pooja Yadav",
        "Kunal Mishra", "Meera Iyer", "Aditya Jain", "Simran Kaur",
        "Harsh Vyas", "Nidhi Saxena", "Yash Malhotra", "Tanvi Desai"
    ],

    "Age": [18, 19, 20, 18, 21, 19, 20, 18, 22, 19,
            20, 21, 18, 19, 22, 20, 21, 18, 19, 20],

    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],

    "Course": [
        "BCA", "B.Tech", "BSc", "BCom", "BCA",
        "BBA", "BSc", "B.Tech", "BCA", "BCom",
        "BBA", "BSc", "B.Tech", "BCA", "BCom",
        "BBA", "BSc", "B.Tech", "BCA", "BCom"
    ],

    "Marks": [85, 92, 78, 88, 81, 95, 73, 89, 90, 76,
              84, 91, 79, 87, 82, 93, 75, 86, 88, 80],

    "City": [
        "Delhi", "Mumbai", "Pune", "Indore", "Jaipur",
        "Bhopal", "Surat", "Chennai", "Hyderabad", "Lucknow",
        "Nagpur", "Patna", "Kolkata", "Ahmedabad", "Kanpur",
        "Ranchi", "Noida", "Nashik", "Vadodara", "Udaipur"
    ]
}

df = pd.DataFrame(students)
# convert to csv without extra index column
df.to_csv("student_data_3.csv",index=False)
