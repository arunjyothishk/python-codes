from numpy import array,real

n=input("Enter the number of elements: ")
a=list()
# print(list())

for i in range(int(n)):
    a.append(complex(input("Elements: ")))
arr0=array(a)
# arr1=real(arr0)
arr2=array(arr0,dtype=int)
print("Entered complex number array is : \n",arr0)
print("Integer Array : \n",arr2)
mul=arr0*arr2
print("multiplying complex array with 3+4j gives :\n",mul)