"""Write a program to calculate the bill amount, in cents, for the units of power consumed. Following are the rates applicable:

1. First 0-100 units: 60 cents per unit
2. Next 200 units: 70 cents per unit
3. Beyond 300 units: 80 cents per unit

The program should accept three different usage unit readings.

Example

If the following inputs are supplied:

305
180
120

Then, the output should be:

20400
11600
7400
:w

Note: You should assume that input to the program is from console input (raw_input) """
print('Enter The First Reading:')
R1 = int(input())
print('Enter The Second Reading:')
R2 = int(input())
print('Enter The Third Reading:')
R3 = int(input())

if R1>100:
	if R1 > 300:
		Bill_1 = ((R1 - 300) * 80) + (200 * 70) + (100 * 60)
	else:	
		Bill_1 = ((R1 - 100) * 70) + (100 * 60)
print(Bill_1)		

if R2>100:
	if R2 > 300:
		Bill_2 = ((R2 - 300) * 80) + (200 * 70) + (100 * 60)
	else:	
		Bill_2 = ((R2 - 100) * 70) + (100 * 60)
print(Bill_2)		

if R3>100:
	if R3 > 300:
		Bill_3 = ((R3 - 300) * 80) + (200 * 70) + (100 * 60)
	else:	
		Bill_3 = ((R3 - 100) * 70) + (100 * 60)
print(Bill_3)		