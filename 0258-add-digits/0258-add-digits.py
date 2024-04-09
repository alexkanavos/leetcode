class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num_string: str = str(num)
            digits: List[int] = [int(digit) for digit in num_string]
            num: int = sum(digits)
        return num