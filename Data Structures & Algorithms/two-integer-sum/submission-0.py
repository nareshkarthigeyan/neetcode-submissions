class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in f:
                return [f[diff], i]
            f[v] = i 