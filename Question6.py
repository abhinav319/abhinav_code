'''Define a function sum() and a function multiply() that sums and
multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10, and 
multiply([1, 2, 3, 4]) should return 24.'''

def addition(list1):
    add=0
    for a in list1:
        add=add+a
    return add

def multiplies(list2):
    multi=1
    for i in list2:
        multi=multi*i
    return multi

obj=addition([1,2,3,4])
obj1=multiplies([1,2,3,4])
print("add is :",obj)
print("mul is :",obj1)
