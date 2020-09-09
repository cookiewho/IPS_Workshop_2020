'''
Let's call an integer a palindrome if it remains the same after
reading its digits from right to left. Given a four-digit
integer, print "YES" if it's a palindrome and print "NO" otherwise. 
'''
a = input()
if (a[:2] == a[-1:1:-1]):
  print("YES")
else:
  print("NO")
