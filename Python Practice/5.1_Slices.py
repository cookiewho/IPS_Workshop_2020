'''
In the first line, print the third character of this string.
In the second line, print the second to last character of this string.
In the third line, print the first five characters of this string.
In the fourth line, print all but the last two characters of this string.
In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
In the seventh line, print all the characters of the string in reverse order.
In the eighth line, print every second character of the string in reverse order, starting from the last one.
In the ninth line, print the length of the given string.:

'''
s = input()
print(s[2])   #1
print(s[-2])  #2
print(s[0:5]) #3
print(s[0:-2])#4
print(s[::2]) #5
print(s[1::2])#6
print(s[::-1])#7
print(s[::-2])#8
print(len(s)) #9