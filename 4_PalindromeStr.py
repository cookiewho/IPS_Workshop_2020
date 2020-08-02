def isPalindrome(string):
  newstr = ""
  string = string.lower()
  for ind in range(len(string)):
    if ord(string[ind]) >= 97 and ord(string[ind]) <=122:
      newstr = newstr + string[ind]
  print(newstr)
  return newstr == newstr[::-1]

print(isPalindrome("Race Car"))
print(isPalindrome("Race a Car"))
print(isPalindrome("otto"))
print(isPalindrome("A man, a plan, a canal, Panama."))