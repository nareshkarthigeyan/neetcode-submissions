class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        st = []
        for c in s:
            if c in bracks.keys() and st and st[-1] == bracks[c]:
                st.pop()
                continue
            st.append(c)

        return len(st) == 0