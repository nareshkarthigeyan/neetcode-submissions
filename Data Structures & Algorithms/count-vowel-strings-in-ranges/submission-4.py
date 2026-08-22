class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        prefix = [0]
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1] + 0)
        output = [prefix[end + 1] - prefix[start] for start, end in queries]
        return output