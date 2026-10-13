import pandas as pd
df = pd.read_csv("C:/Users/HP/OneDrive/Documents/pythonpractice/bankinhg management/__pycache__/pandasss.csv")
print('connected ')

# addinng new column
df['Company']='Amazon'
print(df)
df['Promotion_status']='Promoted'
df['Promotion_status']=df['Promotion_status'].where(df['Age']>=40,'Not promoted')
print(df)

# 10 methods of pandas
# 1. head()
# Shows the first 10 rows
print("\n1. First 10 Records:")
print(df.head(10))
# 2. tail()
# Shows the last 10 rows
print("\n2. Last 10 Records:")
print(df.tail(10))
# 3. describe()
# Shows statistical information about numerical columns
print("\n3. Statistical Information:")
print(df.describe())
# 4. isnull().sum()
# Counts the missing values in each column
print("\n4. Missing Values:")
print(df.isnull().sum())
# 5. fillna()
# Fills missing Age values with the average Age
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("\n5. Age After Filling Missing Values:")
print(df["Age"])
# 6. sort_values()
# Sorts employees according to Salary from highest to lowest
print("\n6. Employees Sorted by Salary:")
print(df.sort_values("Salary", ascending=False))
# 7. value_counts()
# Counts the number of employees in each Department
print("\n7. Number of Employees in Each Department:")
print(df["Department"].value_counts())
# 8. groupby()
# Finds the average Salary of each Department
print("\n8. Average Salary of Each Department:")
print(df.groupby("Department")["Salary"].mean())
# 9. loc[]
# Finds employees whose Salary is greater than 80000
print("\n9. Employees with Salary Greater Than 80000:")
print(df.loc[df["Salary"] > 80000])
# # 10. drop()
# # Removes the Company column
# df = df.drop("Company", axis=1)
print("\n10. Data After Removing Company Column:")
print(df.iloc[6])
# df.to_csv('C:\Users\HP\OneDrive\Documents\pythonpractice\bankinhg management\__pycache__\newpanda.csv')

 