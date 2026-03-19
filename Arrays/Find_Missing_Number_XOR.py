
# class MissingNumber:
#     def __init__(self):
#         self.num = None
#         self.arr = None 
    
#     def find_missing_number(self, nums):
#         xor = 0
#         n = len(nums)
#         for i in range(n + 1):
#             xor ^= i
#         for num in nums:
#             xor ^= num
#         return xor
# # Example usage:
# nums = [0, 1, 3]
# missing_number_finder = MissingNumber()
# missing_number = missing_number_finder.find_missing_number(nums)    
# print(missing_number)  # Output: 2  

class MissingNum():
    def __init__(self):
        self.num = None
        self.arr = None
        
    def MissingNumber(self, num, arr):
        xor1 = 0
        xor2=0
        for i in range (len(arr)):
            xor2 ^= arr[i]
            xor1 ^= i
        xor1 ^= num
        return xor1 ^  xor2
# Example usage:
num = 4
arr = [0, 1, 3, 2]
missing_number_finder = MissingNum()
missing_number = missing_number_finder.MissingNumber(num, arr)
print(missing_number)  # Output: 4