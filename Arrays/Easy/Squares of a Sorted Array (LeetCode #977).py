class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left = 0
        right = len(nums)-1
        
        for i in reversed(range(len(nums))):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else: 
                result[i] = nums[right] ** 2
                right -= 1
        return result

# Time Complexity -> O(n)
# Space Complexity -> O(n)