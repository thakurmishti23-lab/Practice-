import numpy as np
data=np.genfromtxt('C:/Users/HP/OneDrive/Documents/pythonpractice/bankinhg management/100000_employee_data.csv', delimiter=',',dtype=None,encoding='utf-8',names=True)
print(data)

# Total number of employees
# print("Total Employees:", len(data))

# Average employee age
# print("Average Age:", data["age"].mean())

# Average salary
# print("Average Salary:", data["salary"].mean())

# youngest emp
index = np.argmin(data["age"]) 
print("Youngest employee: ") 
print(data[index])

# oldest emp
index = np.argmax(data["age"])                       
print("Oldest Employee: ")
print(data[index])

# count excellent performers
excellent = data["performance"] == "Excellent"
count = np.sum(excellent)
print(" Number of Excellent Performers: ")
print(count)

# dep, emp with need of improvement
departments = np.unique(data["department"])
print(" Needs Improvement Employees by Department: ")
for department in departments:
    condition = ((data["department"] == department) & (data["performance"] == "Needs Improvement") )
    count = np.sum(condition)
    print(department, ":", count)

# highest paid emp
index = np.argmax(data["salary"])
print(" Highest Paid Employee: ")
print(data[index])

# avg salary of each dep
departments = np.unique(data["department"])
print(" Average Salary by Department: ")
for department in departments:
    department_data = data["salary"][data["department"] == department]
    average_salary = np.mean(department_data)
    print(department, ":", average_salary)

# avg experience of each dep
print(" Average Experience by Department:")
for department in departments:
    department_data = data["experience"][data["department"] == department]
    average_experience = np.mean(department_data)
    print(department, ":", average_experience)

# high salary with low performance
average_salary = np.mean(data["salary"])
condition = ((data["salary"] > average_salary)&(data["performance"] == "Needs Improvement"))
result = data[condition]
print(" High Salary but Needs Improvement Employees: ")
print(result)

# excellent perf by dep
print(" Excellent Performance Percentage by Department: ")
for department in departments:
    total = np.sum(data["department"] == department)
    excellent = np.sum((data["department"] == department) &(data["performance"] == "Excellent"))
    percentage = (excellent / total) * 100
    print(department, ":", percentage, "%")

# top 10 highly paid emp
sorted_index = np.argsort(data["salary"])
top_10_index = sorted_index[-10:][::-1]
print(" Top 10 Highest Paid Employees: ")
print(data[top_10_index])

# city with most emp
cities, counts = np.unique(data["City"], return_counts=True)
index = np.argmax(counts)
print(" City with Most Employees: ")
print("City:", cities[index])
print("Employees:", counts[index])

# emp with highest experience
index = np.argmax(data["experience"])
print(" Most Experienced Employee:")
print(data[index])

# emp with less than 3yrs experience
result = data[data["experience"] < 3]
print(" Employees with Less Than 3 Years Experience:")
print(result)

# emp with more than 10yrs exp
result = data[data["experience"] > 10]
print(" Employees with More Than 10 Years Experience:")
print(result)