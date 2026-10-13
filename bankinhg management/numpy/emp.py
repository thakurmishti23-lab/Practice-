import csv
import random

first_names = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Kabir",
    "Rohan", "Rahul", "Karan", "Ankit", "Mohit",
    "Yash", "Aman", "Neha", "Priya", "Ananya",
    "Isha", "Kavya", "Sneha", "Pooja", "Riya"
]

last_names = [
    "Sharma", "Verma", "Thakur", "Singh", "Kumar",
    "Gupta", "Mehta", "Kapoor", "Joshi", "Chauhan"
]

cities = [
    "Shimla", "Delhi", "Chandigarh", "Mumbai", "Bangalore",
    "Kolkata", "Pune", "Jaipur", "Lucknow", "Dehradun"
]

departments = [
    "IT", "HR", "Finance", "Marketing",
    "Sales", "Operations", "Support"
]

performance = [
    "Excellent", "Good", "Average", "Needs Improvement"
]

with open("100000_employee_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # column names
    writer.writerow([
        "id",
        "name",
        "age",
        "city",
        "department",
        "salary",
        "experience",
        "performance"
    ])

    # 100000 rows
    for i in range(1, 100001):

        name = random.choice(first_names) + " " + random.choice(last_names)
        age = random.randint(21, 60)
        city = random.choice(cities)
        department = random.choice(departments)
        salary = random.randint(25000, 150000)
        experience = random.randint(0, 30)
        result = random.choice(performance)

        writer.writerow([
            i,
            name,
            age,
            city,
            department,
            salary,
            experience,
            result
        ])

print("100000 rows CSV file created successfully!")