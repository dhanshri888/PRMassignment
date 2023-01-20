#Q1.You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. 
# You have to sort the list based on 2nd last character of a string.


l = ['great','hello','hiyo','abc']
l.sort(key= lambda x: x[-2])
print(l)


