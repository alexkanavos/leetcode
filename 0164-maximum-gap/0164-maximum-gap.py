class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length: int = len(nums)
        max_diff: int = 0
        if length < 2:
            return max_diff
        else:
            nums = sorted(nums)
            for i in range(1, length):
                if nums[i] - nums[i-1] > max_diff:
                    max_diff = nums[i] - nums[i-1]
        return max_diff
                