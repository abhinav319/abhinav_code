'''Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, 
but writing it yourself is nevertheless a good exercise.)'''

def length(a):
    digit = 0
    for x in a:
        digit=digit+1
    return digit

a= input("Enter the name :")
print("The length is ",length(a))
