''' Write a program that given a text file will create a new text file in which all
the lines from the original file are numbered from 1 to n (where n is the number of
lines in the file). '''

file = open("Question34.txt","r")
newfile = open("abhinav.txt","w")
txt = file.readlines()

count = 0
for line in txt:
    count+=1
    output_line = str(count)+". "+line
    newfile.write(output_line)

print("success fully create")
file.close()
newfile.close()