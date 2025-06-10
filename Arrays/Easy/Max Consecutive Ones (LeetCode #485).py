class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                if current > result:
                    result = current 
            else:
                current = 0
        return result

# Time complexiy -> O(n)
# Space complexity -> O(1)
        