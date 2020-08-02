def minimumCharacters(string):
  new_str = string
  count = 0
  while(string != string[::-1]):
      new_str = string[-1:-(count +1):-1] + string
      if new_str == new_str[::-1]:
          return count
      count+=1
  return count
  
string1 = "ABC"
string2 = "AACECAAAA"
string3 = "DEFG"
string4 ="AACECAAAAAAC"
print(minimumCharacters(string1))
print(minimumCharacters(string2))
print(minimumCharacters(string3))
print(minimumCharacters(string4))