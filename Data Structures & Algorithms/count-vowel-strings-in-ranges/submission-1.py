class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        prefix = []
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prefix.append(1)
            else:
                prefix.append(0)
        output = [sum(prefix[start:end + 1]) for start, end in queries]
        return output



        # for q in queries:
        #     start, end = q
        #     count = 0
        #     for i in range(start, end + 1):
        #         w = words[i]
        #         if w[0] in vowels and w[-1] in vowels:
        #             count += 1
        #     output.append(count)
        # return output