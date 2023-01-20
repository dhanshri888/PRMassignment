#Q2. checking validity of triangle
def checkValid_triangle(a, b, c):
    if ((a*a)+(b*b)==(c*c)):
        return True
    else: 
        return False       
  
#driven code 
a = 3
b = 4
c = 5
if checkValid_triangle(a, b, c): 
    print("Valid")  
else: 
    print("Invalid") 

# checking validity of rectangle
def checkvalid_rectangle(a,b,c,d):
    if ((a==c)&(b==d)):
        return True
    else:
        return False

#driven code
a = 2 
b = 4
c = 2
d = 4
if checkvalid_rectangle(a,b,c,d):
    print("valid")
else:
    print("invalid")