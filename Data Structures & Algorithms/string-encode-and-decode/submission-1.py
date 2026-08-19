class Solution:

    def encode(self, strs: List[str]) -> str:
        ss = ""
        if strs:
            for s in strs:
                ss += f"{len(s)}#"
                ss += s
        ss += "f#"
        return ss
        
    def decode(self, s: str) -> List[str]:
        ss = ""
        strs = []
        end = False
        i = 0
        tlength = 0
        while i < len(s):
            if s[i:].startswith("f#"):
                end = True
                break
            
            if s[i].isdigit():
                tlength *= 10
                tlength += int(s[i])

            if s[i] == "#":
                if tlength == 0:
                    strs.append("")
                    i += 1
                else:
                    strs.append(s[i + 1:i + tlength + 1])
                    i += tlength + 1
                tlength = 0
                continue
            
            i += 1
        return strs
            


            