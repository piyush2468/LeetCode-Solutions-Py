from collections import Counter
class Solution(object):

def getHint(self, secret, guess):
"""
:type secret: str
:type guess: str
:rtype: str
"""

    bull_count = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull_count += 1
        secret_counter = Counter(secret)
        guess_counter = Counter(guess)
        cow_count = sum((secret_counter & guess_counter).values()) - bull_count
        return "{0}A{1}B".format(bull_count, cow_count)





