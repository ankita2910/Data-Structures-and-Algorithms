
class TwoSumOptimal:
    def two_sum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []  # Return an empty list if no solution is found
# Example usage:
nums = [2, 7, 11, 15]
target = 9
two_sum_solver = TwoSumOptimal()
result = two_sum_solver.two_sum(nums, target)
print(result)  # Output: [0, 1]     
# Here the time complexity is O(n) because we are iterating through the array once, and 
# the space complexity is O(n) in the worst case when all elements are unique and stored in the hash map.