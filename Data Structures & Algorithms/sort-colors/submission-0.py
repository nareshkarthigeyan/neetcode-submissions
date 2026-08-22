from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)
        red = freq[0]
        white = red + freq[1]
        blue = white + freq[2]

        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < white:
                nums[i] = 1
            else:
                nums[i] = 2