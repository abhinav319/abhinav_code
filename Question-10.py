'''Define a function overlapping() that takes two lists and returns True if they have at
least one member in common, False otherwise. You may use your is_member() function, or the
in operator, but for the sake of the exercise, you should (also) write it using two
nested for-loops.'''
def overlapping(list1,list2):
    for x in list1:
        for z in list2:
            return True
    return False
a=[4,8,12,16]
b=[5,3,7,8]
obj=overlapping(a,b)
print(obj)
