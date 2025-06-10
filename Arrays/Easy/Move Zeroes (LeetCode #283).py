class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        temp = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left += 1
        return nums

# time complexity of the code -> O(n)
# space complexity of the code -> O(1)