class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ends_at = [(x, (target - x) / y) for x, y in zip(position, speed)]
        ends_at = sorted(ends_at, key = lambda x: x[0], reverse = True)
        st = []
        fleet = 0
        for car, ends in ends_at:
            if not st or ends > st[-1][-1]:
                st.append((car, ends))
        return len(st)