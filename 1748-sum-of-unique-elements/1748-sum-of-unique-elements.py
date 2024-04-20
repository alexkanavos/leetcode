class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums = [num for num in nums if nums.count(num) == 1]
        return sum(nums)
        