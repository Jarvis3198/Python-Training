"""Program to obtain a value from a dictionary,
without having to handle an exception if the key you seek is not in the dictionary."""

#Using the get method

dict = { 'a' : 1 , 'b' : 2 , 'c' : 3 , 'd' : 4} 

print (dict.get('a', "Not Present")) 
print (dict.get('b', "Not Present")) 
print (dict.get('c', "Not Present"))
print (dict.get('d', "Not Present"))
print (dict.get('e', "Not Present")) 