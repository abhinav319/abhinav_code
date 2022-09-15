'''Write a function that takes a character (i.e. a string of length 1) 
and returns True if it is a vowel, False otherwise.'''

def Vowel(x):
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        return True
    else:
        return False

x = input("Enter The string :")
obj = Vowel(x)
print(obj)
