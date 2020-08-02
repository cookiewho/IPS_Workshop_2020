def longest_palindrome(input_string):
  longest = ""
  for x in range(len(input_string)):
    for y in range(x, len(input_string)):
      if input_string[x] == " ":
        continue
      temp = input_string[x:y+1]
      if temp == temp[::-1]:
        if len(temp) > len(longest):
          longest = temp
  return longest
s1 ="i want to be a racecar driver"
s2 = "ac"
print("longest = " + longest_palindrome(s1))
print("longest = " + longest_palindrome(s2))