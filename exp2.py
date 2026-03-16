import numpy as np

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print("Array A:\n",A)
print('Array B:\n',B)
result1=np.dot(A,B)
print("Multiplication of two 2x2 Matrix:\n",result1)
C=np.array([[1,2],[3,4],[5,6]])
print("Array C:\n",C)
trans=C.T
result2=np.dot(trans,C)
print("Transpose:\n",trans)
print("Dot product after transpose:\n",result2)