import numpy as np  
n=input("number of elements")
a=[]
# print(list())

for i in range(int(n)):
    a.append(input("elements: "))
arr=np.array(a)
arr1=np.real(arr)
arr2=np.array(arr1,dtype=int)
print("Entered complex array is : \n",arr)
print("Integer Array : \n",arr2)
ans=(3+4j)*arr
print("multiplying coupler array with 3+4j gives :\n",ans)