'''
 There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. 

"joey" -> "joe"
"pale" -> "ple"
"pale" -> "bake"
"joey" -> "ple"
"jo" -> "joey"

count =0
if abs(len(s1) - len(s2)) > 1:
  return False #catches len diff > 1
if len(s1) < len(s2): # get min len
  mins_str = len(s1)
else:
  min_str = len(s2)
loop through the min_str: #looping through and checking if both string at that spot are ==
if s1 != s2: 
  count+=1 
  want to chek the next value in str to see if ==
  if yes count mistaken string index up one
'''
def validEdit(s1, s2):
  count = 0
  if abs(len(s1) - len(s2)) > 1:
    return False #catches len diff > 1
  '''if len(s1) < len(s2): # get min len
    mins_str = len(s1)
  elif len(s2) < len(s1):
    mins_str = len(s2)
  else:
    min_str = len(s2)
    '''
  x = 0
  y = 0
  #for x in range(len(min_str)): #looping through and checking if both string at that spot are ==
  while x < len(s1) and y < len(s2):
    if s1[x] != s2[y]: 
      if (x+1 < len(s1)) and (s1[x+1] == s2[y]):
        count+=1
        x+=2
        y+=1
      elif (y+1 < len(s2)) and (s2[y+1] == s1[x]):
        count+=1
        y+=2
        x+=1
      else:
        count+=1
        x+=1
        y+=1
    else:
      x+=1
      y+=1
  if count > 1:
    return False
  else:
    return True

print(validEdit("joey", "joe"))     #true
print(validEdit("pale", "ple"))     #true
print(validEdit("pale", "bake"))    #false
print(validEdit("joey", "ple"))     #false
print(validEdit("jo", "joey"))      #false
print(validEdit("pale", "bale"))    #true
print(validEdit("pales", "pale"))   #true
print(validEdit("cookie", "cokie")) #true
