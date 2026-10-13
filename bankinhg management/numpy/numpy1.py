import numpy as np
# a=[[1,4,8,12,16,20]]
# b=np.array(a)
# print(b.ndim)               # dim represents the dimensions

# arr=np.zeros(10, dtype=int)
# print(arr)

# arr1=np.ones(10, dtype=int)
# print(arr1)

# arr2=np.arange(1,19)
# print(arr2)

# arr3=arr2.astype(float)
# print(arr3)

data=np.array([[15,30,45,60],
              [10,20,30,40],
              [20,40,60,80]])
# print(data)  
# total_sum_c=np.sum(data, axis=1)              #for columns
# print(total_sum_c)

# total_sum_r=np.sum(data, axis=0)              #for rows
# print(total_sum_r)

mean=np.mean(data)
print(mean)

mean_c=np.mean(data, axis=1)
print(mean_c)

mean_r=np.mean(data, axis=0)
print(mean_r)