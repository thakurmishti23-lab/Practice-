import pandas as pd
data1=pd.read_csv('C:/Users/HP/OneDrive/Documents/pythonpractice/bankinhg management/100000_employee_data.csv')
# print(data1)
data2=pd.read_csv('C:/Users/HP/OneDrive/Documents/pythonpractice/bankinhg management/__pycache__/pandasss.csv')
# print(data2)

# Inner merge 
inner = pd.merge(data1, data2, on='ID', how='inner')
print(" \n Inner Merge:-")
print(inner)

# Left merge 
left = pd.merge(data1, data2, on='City', how='left')
print(" \n Left Merge:")
print(left)


