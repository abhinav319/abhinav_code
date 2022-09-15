'''Define a function max() that takes two numbers as arguments and returns the largest 
of them.Use the if-then-else construct available in Python. (It is true that Python has 
the max()function built in, but writing it yourself is nevertheless a good exercise.)'''


def large(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return None

if __name__ == '__main__':
    print("largest number is",large(5,8))
    print("largest number is",large(15,6))
    print("largest number is",large(10,10))
