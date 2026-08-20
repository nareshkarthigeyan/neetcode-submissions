class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i, v in enumerate(numbers):
            diff = target - v
            if diff in h.keys():
                return [h[diff] + 1, i + 1]
            h[v] = i