class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans: list[int] = []
        while nums:
            temp: set = set(nums)
            for i in temp:
                if i in nums:
                    nums.remove(i)
            ans.append(list(temp))
        return ans