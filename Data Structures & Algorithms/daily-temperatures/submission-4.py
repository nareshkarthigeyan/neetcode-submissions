class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        st = [] # pair: (temp, index)
        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                temp, index = st.pop()
                out[index] = i - index
            st.append((t, i))
        return out