class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for k in nums[i+1::]:
                if num + k == target:
                    return [i, nums[i+1::].index(k) + i + 1]