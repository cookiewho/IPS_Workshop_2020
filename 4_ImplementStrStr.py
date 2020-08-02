def strStr(haystack, needle):
  for x in range(len(haystack)-(len(needle))+1):
    if haystack[x:(x+len(needle))] == needle:
      return x
  return -1
haystack1 = "hello"
needle1 = "ll"
haystack2 = "aaaaa"
needle2 = "bba"
print(strStr(haystack1,needle1))
print(strStr(haystack2,needle2))