class Solution(object):

def getHint(self, secret, guess):
"""
:type secret: str
:type guess: str
:rtype: str
"""

    cnt, common = 0, set(secret)&set(guess)
    for c in common:
        cnt += min(secret.count(c),guess.count(c))
    b = sum([secret[i]==guess[i] for i in range(len(guess))])
    return str(b) + 'A'  +str(cnt-b) + 'B'
