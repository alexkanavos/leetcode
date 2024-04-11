class Solution:
    def isHappy(self, n: int) -> bool:
        seen: List[int] = []
        while n != 1 and n not in seen:
            seen.append(n)
            n: str = str(n)
            n: List[int] = [int(digit) * int(digit) for digit in n]
            n: int = sum(n)
        return n == 1