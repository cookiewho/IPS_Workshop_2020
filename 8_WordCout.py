def count_words(text):
  words = []
  temp_word = ""
  text = text.lower() + " "
  for char in text:                                 # could text.split(), but that would require some clean up, 
    if char == '-' or (char >= 'a' and char <= 'z'):# and could potentially lead to more headache/ running into
      temp_word += char                             # certain problematic edge cases, hence why I opted for a "messier" solution
    else:
      if len(temp_word) > 0:
        words.append(temp_word)
      temp_word = ""
  dictionary = {}
  for word in sorted(words):
    if word in dictionary:
      dictionary[word] += 1
    else:
      dictionary[word] = 1
  string = ""
  for key, value in dictionary.items():
    string += str(key) + " " + str(value) + "\n"
  return string
sen = "I do not like green eggs and ham, I do not like them, Sam-I-Am"
print(count_words(sen))