from numpy import array,zeros,arange
import time
list_1=arange(0,1000,dtype=int)
arr1=array(list_1)
# list_1.reverse()
arr2=array(list_1)
# print(arr1)
# print(arr2)

zero_arr=zeros(len(arr1),dtype=int)
time_init=time.time()
for i in range (len(arr1)):
    zero_arr[i] = arr1[i] + arr2[i]
time_end=time.time()
time_diff=time_end-time_init
# print("classic method result : ",zero_arr," Time taken to process : ", time_diff)
print("process time with loop: ",time_diff)
time_init=time.time()
arr3=arr1+arr2
time_end=time.time()
time_diff=time_end-time_init
# print("Numpy array sum result: ",arr3,"process time: ",time_diff)
# print(arr3)
print("process time with numpy-array: ",time_diff)
