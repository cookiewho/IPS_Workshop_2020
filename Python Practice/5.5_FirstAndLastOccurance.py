'''
Given a string that may contain a letter f. Print the index of the first
and last occurrence of f. If the letter f occurs only once, then output
its index once. If the letter f does not occur, print -1.
'''
s = input()
ind1 = ind2 = -1
for x in range(len(s)):
  if s[x] == 'f':
    if ind1 == -1:
      ind1 = x
      ind2 = x
    else:
      ind2 = x
if ind1 == ind2:
  print(ind1)
else:
  print(ind1, ind2)
