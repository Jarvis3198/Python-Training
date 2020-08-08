"""Write a program which takes 4 inputs, where each input consists of 2 numbers in the format x,y.
You are required to print a two dimensional array having x rows and y columns for each input.
The elements of the arrays should be whole numbers starting from 1 and incrementing by 1.

Example

Suppose the following 4 inputs are given to the program:

2,2
2,3
3,3
3,4

Then, the output of the program should be:

[[1, 2], [3, 4]]
[[1, 2, 3], [4, 5, 6]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

Note: You should assume that input to the program is from console input (raw_input) """

import numpy as np


print('Enter The First Dimension:')
D1 = input().split(",")
print('Enter The Second Dimension:')
D2 = input().split(",")
print('Enter The Thrid Dimension:')
D3 = input().split(",")
print('Enter The Fourth Dimension:')
D4 = input().split(",")

num = 1
M1 = np.zeros((int(D1[0]),int(D1[1])))

for row in range (0,int(D1[0])):
	for col in range(0,int(D1[1])):
		M1[row][col] = num
		num += 1
	
print(M1)	

num = 1
M2 = np.zeros((int(D2[0]),int(D2[1])))

for row in range (0,int(D2[0])):
	for col in range(0,int(D2[1])):
		M2[row][col] = num
		num += 1
	
print(M2)	

num = 1
M3 = np.zeros((int(D3[0]),int(D3[1])))

for row in range (0,int(D3[0])):
	for col in range(0,int(D3[1])):
		M3[row][col] = num
		num += 1
	
print(M3)	

num = 1
M4 = np.zeros((int(D4[0]),int(D4[1])))

for row in range (0,int(D4[0])):
	for col in range(0,int(D4[1])):
		M4[row][col] = num
		num += 1
	
print(M4)	
		