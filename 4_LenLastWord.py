###NEW AND IMPROVED SOLUTION, MUCH MORE EFFICEINT###
def lengthOfLastWord(string):
  for x in range(len(string)):
    if string[x] == " ":
      count = 0
      for y in range(x+1,len(string)):
        if string[y] == " ":
          x = y
          break
        else:
          count += 1 
      return count
  return 0
sampleInput = "Hello World"
print(lengthOfLastWord(sampleInput))

def length_of_last_word(words):
  ###OLD SOLUTION, BAD AND ICKY AND INEFFICIENT###
  start = 0
  stop = -1
  found = False
  if(len(words) == 0):
    return 0
  for x in range(len(words)):
    if ord(words[x]) != 32 and found == True:
      print("start "+ str(x))
      start = x
      found = False
    elif ord(words[x]) != 32 and found == False:
      print("stop "+ str(x))
      stop = x
    if ord(words[x]) == 32:
      found = True
  if start > stop and ord(words[start]) != 32: 
    stop = start
  print(words[start:stop+1])
  return len(words[start:stop+1])
  
s1 = "Lebz Q"
s2 = "    "
s3 = ""
s4 = "  xDGBklKecz IAcOJYOH O  WY WPi"
print(length_of_last_word(s1))
print("next eexample")
print(length_of_last_word(s2))
print("next eexample")
print(length_of_last_word(s3))
print("next eexample")
print(length_of_last_word(s4))