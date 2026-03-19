#The other elements in the array appear twice

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result   
# Example usage:
nums = [4, 1, 2, 1, 2]
solution = Solution()               
single_number = solution.singleNumber(nums)
print(single_number)  # Output: 4   

#Here the time complexity is O(n) and the space complexity is O(1)