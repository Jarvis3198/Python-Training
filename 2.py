"""Program to construct a new list by operating on elements of an existing sequence.

USING List Comprehensions

    For Example.

        List1=[1,2,3,4,5]

        operation to perform : x*5

        so new list will be [5,10,15,20,25]
"""

List1=[1,2,3,4,5] 
NewList = [i * 5 for i in List1] 



print(NewList)