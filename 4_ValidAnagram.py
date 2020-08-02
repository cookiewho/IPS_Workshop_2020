def valid_anagram(s,t):
  return sorted(s) == sorted(t)
l = "anagram"
m = "nagaram"
n = "rat"
o = "car"

print(valid_anagram(l,m))
print(valid_anagram(n,o))