class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good: list[tuple] = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    good.append((i, j))
        return len(good)