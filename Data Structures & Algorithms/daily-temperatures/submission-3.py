class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        st = []
        for i, v in enumerate(temperatures):
            while st and v > st[-1][-1]:
                output[st[-1][0]] = i - st[-1][0]
                st.pop()
            st.append((i, v))
        return output
            