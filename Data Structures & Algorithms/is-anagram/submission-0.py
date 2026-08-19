from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(s)
        for c in t:
            freq[c] = freq.get(c, 0) - 1
        return all(x == 0 for x in freq.values())