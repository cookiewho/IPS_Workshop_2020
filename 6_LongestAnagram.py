def longest_anagram(string, dictionary):
  string = sorted(string)
  m_len = 0
  ans = ""
  for word in dictionary:
    temp2 = word[:]
    word = sorted(word)
    count = 0
    for x in range(len(string)):
      if string[x] == word[0]:
        word.pop(0)
        count += 1
      if len(word) == 0:
        break
    if len(word) == 0:
      if count > m_len:
        m_len = count
        ans = temp2
  return ans
  
dict = ["bat", "aman", "antman"]
string = "batman"
print(longest_anagram(string, dict))