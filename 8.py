"""Write a program that accepts a comma separated sequence of words as input and prints the words in a comma separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

order,hello,would,test

Then, the output should be:

hello,order,test,would

Note: You should assume that input to the program is from console input (raw_input)

"""


print('Enter The Words:')
Words = input().split(",")

Words.sort()

for word in Words:
	print(word, end = " ")