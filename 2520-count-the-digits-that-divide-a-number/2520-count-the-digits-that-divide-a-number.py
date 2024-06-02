class Solution:
    def countDigits(self, num: int) -> int:
        dividers: list[chr] = [i for i in str(num) if int(i) != 0 and num % int(i) == 0]
        return len(dividers)