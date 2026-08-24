class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ends_at = sorted([(x, (target - x) / y) for x, y in zip(position, speed)], key = lambda x: x[0], reverse=True)
        stack = []
        for car, ends in ends_at:
            if not stack or ends > stack[-1][-1]:
                stack.append((car, ends))
        return len(stack) 