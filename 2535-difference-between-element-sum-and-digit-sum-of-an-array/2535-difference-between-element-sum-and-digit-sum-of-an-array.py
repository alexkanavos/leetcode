class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum: int = sum(nums)
        digit_sum: int = 0
        digits: list[str] = [str(i) for i in nums]
        for d in digits:
            if len(d) == 1:
                digit_sum += int(d)
            else:
                d: list[str] = list(d)
                d: list[int] = [int(j) for j in d]
                d: int = sum(d)
                digit_sum += d
        return abs(el_sum - digit_sum)