''' Define a procedure histogram() that takes a list of integers and 
prints a histogram to the screen. For example, histogram([4, 9, 7]) 
should print the following:
****
*********
******* '''

def histogram(lst):
    for i in lst:
        print(i * '*')

lst1 = []
lst2 = int(input("How many Number for create list:"))
for x in range(lst2):
    data = int(input("Enter the list :"))
    lst1.append(data)
histogram(lst1)
