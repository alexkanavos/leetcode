class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique_elements: set = set(nums)
        n: int = len(nums)
        for num in unique_elements:
            if nums.count(num) > n / 2:
                return num
        