#[ 1 -3 3
#  3 -5 3 
# 6 -6 4 ]

from numpy import linalg,array

matrix = [[ 1 ,-3 , 3 ],[ 3 ,-5 
, 3 ],[ 6, -6, 4 ]]

mat=array(matrix)

eig_value,eig_vector = linalg.eig(mat)

print("Eigen Value : ",eig_value,"\n","Eigen Vector : ",eig_vector)