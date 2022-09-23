'''Write a procedure char_freq_table() that, when run in a terminal, accepts a file
name from the user, builds a frequency listing of the characters contained in the
file, and prints a sorted and nicely formatted character frequency table to the screen.
'''

def char_freq_table(file_name):
  frequency = {}
  with open(file_name, 'r') as f:

    string = filter(lambda x: x not in [' ','\n'], f.read())

    for c in string:
      if c in frequency:
        frequency[c] += 1
      else:
        frequency[c] = 1

    print('Characters frequency listing:')
    for char in sorted(frequency.items(), key=lambda x: x[1]):
      print(char[0], ":",frequency[char[0]])


file_name = "Question34.txt"
char_freq_table(file_name)