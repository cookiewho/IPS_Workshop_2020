def bigram_frequency_analyzer(text):
  text = text.split() #text.split(" ") leads to an extra white space being included in the list, which we dont want
  dict = {}
  for x in range(len(text)-2):
    temp = str(text[x]) + " " + str(text[x+1])
    if temp in dict:
      if text[x+2] in dict[temp]:
        dict[temp][text[x+2]] += 1
      else:
        dict[temp][text[x+2]] = 1
    else:
      dict[temp] = {}
      dict[temp][text[x+2]] = 1
  string = ""
  for key, value in dict.items():
    string += str(key) + " : "
    for key2, value2 in dict[key].items():
      string += str(key2) + " (" + str(value2) + ") "
    string += "\n"
  return string
test = "I do not like green eggs and ham, I do not like them, Sam-I-Am! I do not like them with a fox, I do not like them in a box. I do not like them here or there, I do not like them anywhere! I do not like them, Sam-I-Am, I do not like green eggs and ham!"
test2 = "a b c d e f g h i j k l m n o p q r s t u v w x y z  "# not passing second test case, but displaying correct answer, more testing needed
print(bigram_frequency_analyzer(test))
print(bigram_frequency_analyzer(test2))