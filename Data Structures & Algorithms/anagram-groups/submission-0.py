from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            f[key].append(s)
        return [x for x in f.values()]