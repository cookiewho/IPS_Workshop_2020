'''
Given a string consisting of exactly two 
words separated by a space. Print a new
string with the first and second words swapped:
the second word is printed first. Consider all
adjacent non-space characters a single word.
'''
s = input()
s = s.split(" ")
print(s[1], s[0])
