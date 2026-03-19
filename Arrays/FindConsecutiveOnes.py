
class ConsecutiveOnes:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count
# Example usage:
nums = [1, 1, 0, 1, 1, 1]
consecutive_ones_finder = ConsecutiveOnes()
max_consecutive_ones = consecutive_ones_finder.findMaxConsecutiveOnes(nums)
print(max_consecutive_ones)  # Output: 3    
    