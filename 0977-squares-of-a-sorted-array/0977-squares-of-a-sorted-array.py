class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums: list[int] = [num * num for num in nums]
        return sorted(nums)