'''Define a function max_of_three() that takes three numbers as arguments 
and returns the largest of them.'''

def max_of_three(x,y,z):
    if (x>y) and (x>z):
        return x
    elif (y>x) and (y>z):
        return y
    else:
        return z

obj = max_of_three(15,17,90)
print("max number is",obj)
