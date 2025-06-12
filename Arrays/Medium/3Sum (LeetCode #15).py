class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        nums.sort()

        for traverser in range(len(nums)):
            if nums[traverser] > 0 and nums[traverser] != nums[traverser-0]:
                continue
            left = traverser+1
            right = len(nums) - 1

            while left < right:
                total = nums[traverser] + nums[left] + nums[right]

                if total > 0:
                    right -= 1

                elif total < 0:
                    left += 1
                
                else: 
                    result.append([nums[traverser],nums[left],nums[right]])
                    left += 1
                    
                    while nums[left] == nums[left-1] and left < right:
                        left += 1



                    
        return result
# Time complexity -> O(n2)
# Space complexity -> O(n)