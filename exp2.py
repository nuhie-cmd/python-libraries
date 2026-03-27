import numpy as np #imports numpy library 

A=np.array([[1,2],[3,4]]) #initializing array A
B=np.array([[5,6],[7,8]]) #initializing array B
print("Array A:\n",A) #prints array A
print('Array B:\n',B) #prints array B
result1=np.dot(A,B) #performs dot operation on array A and B
print("Multiplication of two 2x2 Matrix:\n",result1) 
C=np.array([[1,2],[3,4],[5,6]]) #initializing array C
print("Array C:\n",C) #prints array C
trans=C.T #performs transposition on array C
result2=np.dot(trans,C) #performs dot operation on array C and its transposed form
print("Transpose:\n", trans)
print("Dot product after transpose:\n",result2)
