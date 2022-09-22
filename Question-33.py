
"""
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or
phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write
a semordnilap recogniser that accepts a file name (pointing to a list of words) from
the user and finds and prints all pairs of words that are semordnilaps to the screen.
For example, if "stressed" and "desserts" is part of the word list, the the output
should include the pair "stressed desserts". Note, by the way, that each pair by itself
forms a palindrome!

"""


def is_semordnilap(word): 
    file = open(word)
    list_words = file.read().split()
    list1 = []
    for x in list_words:
        for y in list_words:
            if x == y[-1::-1]:
                list1.append(x)
    return list1
print(is_semordnilap("Question-33.txt"))

