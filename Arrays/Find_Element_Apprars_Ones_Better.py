#Here analyse the time complexity and space complexity of the code.
#We will use map to store the count of each element in the array and then find the element which appears only once.
#Here time complexity is O(n) and space complexity is O(n) because we are using a map to store the count of each element in the array.
#While decaring the map the N is length of the array and N  in log N is size of the map which is at most N/2 because we are storing only the elements which appear twice in the array.
# As every number appears twice except for one, the maximum number of unique numbers that can be stored in the map is N/2 (where N is the length of the array). Therefore, the space complexity is O(N/2) which simplifies to O(N).
# Also, we are iterating through the array once to populate the map and then iterating through the map to find the single number, which gives us a time complexity of O(n) + O(n/2) = O(n).
#Hence the time complexity is O(NlogM) + O(N/2+2) where M is the size of the map and N is the length of the array.
#M is at most N/2+1, so the time complexity can be expressed as O(N log (N/2+1)) which simplifies to O(N log N).
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        for num, count in count_map.items():
            if count == 1:
                return num
# Example usage:
nums = [4, 1, 2, 1, 2]      
solution = Solution()
single_number = solution.singleNumber(nums)
print(single_number)  # Output: 4
        