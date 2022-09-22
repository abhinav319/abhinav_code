''' Write a version of a palindrome recogniser that accepts a file name from the user,
reads each line, and prints the line to the screen if it is a palindrome.'''

import re 

def palindrome(word):
    word = re.sub(r'[^a-zA-Z]','',word).lower()
    
    reverse_word =''
    length_word = len(word)
    while length_word>0:
        length_word -= 1
        reverse_word += word[length_word]
    
    if reverse_word == word:
        return True
    else:
        return False

file = open("Question-32.txt", "r")
for x in file.readlines():
    print(x)
    print(palindrome(x))
