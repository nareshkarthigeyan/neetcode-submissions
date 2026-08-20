class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            num1 = numbers[left]
            num2 = numbers[right]
            added = num1 + num2
            if added > target:
                right -= 1

            if added == target:
                return [left + 1, right + 1]
            
            if added < target:
                left += 1
            
        return [left + 1, right + 1]