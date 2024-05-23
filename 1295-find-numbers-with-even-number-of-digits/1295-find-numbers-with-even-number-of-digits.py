class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        lengths: list[int] = [len(str(n)) for n in nums]
        even: list[int] = [1 for l in lengths if l % 2 == 0]
        return len(even)