'''
You are playing the following Bulls and Cows game with your friend:
You write down a number and ask your friend to guess what the number
is. Each time your friend makes a guess, you provide a hint that
indicates how many digits in said guess match your secret number
exactly in both digit and position (called "bulls") and how many
digits match the secret number but locate in the wrong position
(called "cows"). Your friend will use successive guesses and hints
to eventually derive the secret number.

Write a function to return a hint according to the secret number and
friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain
duplicate digits.
'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = list(secret)
        g = list(guess)
        bulls = cows = 0
        dict = {}
        for x in range(len(s)):
            if s[x] == g[x]:
                bulls += 1
            else:
                dict[x] = s[x]
        for y in range(len(s)):
            if s[y] == g[y]:
                continue
            for key, vals in dict.items():
                if vals == g[y]:
                    cows += 1
                    dict.pop(key)
                    break
        return (str(bulls) + "A" + str(cows) + "B")