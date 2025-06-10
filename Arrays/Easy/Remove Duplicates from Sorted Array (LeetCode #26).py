class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(0,len(nums)):
            if nums[right] != nums[left-1]:
                nums[left] = nums[right]
                left += 1
        return left 

# Time complexity -> O(n)
# Space complexity -> O(1)