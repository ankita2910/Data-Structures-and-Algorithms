
class MissingNumber:
    def __init__(self):
        pass
    
    def find_missing_number(self, nums):
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum
# Example usage:
nums = [0, 1, 3]
missing_number_finder = MissingNumber()
missing_number = missing_number_finder.find_missing_number(nums)
print(missing_number)  # Output: 2  