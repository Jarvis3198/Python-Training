
"""Write a program which accepts bank account transactions in a comma separated sequence and prints the net account balance.
The various transactions are classified as deposits (D) and withdrawals (W).
Deposit transactions are suffixed with a hyphen followed by D and Withdrawal transactions are suffixed with a hyphen followed by W.

If the net account balance is more than 5000 dollars, an interest of 5% should be added to the balance. The amount to be printed should be an integer value,
such that if you are getting an output of 4321.0, the program should give the output as 4321.

Example

If following input is supplied to the program:

2000-D,4000-D,500-W

Then, the output of the program should be:

5775

In this example, since the net balance was above $5000, 5 % interest has been added to it.

Note: You should assume that input to the program is from console input (raw_input) """

import sys
balance = 0

print('Enter The Transactions:')
transactions = input().split(",")


for entry in transactions:
	if entry[-1] == "D":
		balance = balance + int(entry[0:-2])
	elif entry[-1] == "W":
		balance = balance - int(entry[0:-2])
	
if balance > 5000:
	balance = balance * 1.05	
print(int(balance))