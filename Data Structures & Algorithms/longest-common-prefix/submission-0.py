class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(min(strs))):
            prefix = strs[0][:i + 1]
            if not all(x.startswith(prefix) for x in strs):
                return strs[0][:i]
        return strs[0][:len(min(strs))]