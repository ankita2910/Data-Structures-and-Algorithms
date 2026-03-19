
class MissingNumber:
    def find_missing_number(self, nums):
        hash_set = set()
        n = len(nums)
        for i in range(1, n + 1):
            hash_set.add(i)
        for num in nums:
            if num in hash_set:
                hash_set.remove(num)
        return hash_set.pop()
# Example usage:
nums = [0, 1, 3]
missing_number_finder = MissingNumber()
missing_number = missing_number_finder.find_missing_number(nums)
print(missing_number)  # Output: 2
