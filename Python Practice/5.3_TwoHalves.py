'''
Given a string, cut it into two equal parts.
If the length of the string is odd, leave the middle character
within the first chunk, so that the first string contains one
more character than the second. Now print a new string on a single
row with the first and second halves swapped: second half first and
the first half last.
'''
s = input()
if(len(s)%2 ==0):
  print(s[len(s)//2:] + s[:len(s)//2])
else:
  print(s[len(s)//2+1:] + s[:len(s)//2+1])
# ALTERNATIVELY
print(s[-(-len(s)//2):] + s[:-(-len(s)//2)])