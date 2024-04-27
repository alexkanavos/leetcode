class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1: list[int] = [i for i in range(1, n + 1) if i % m != 0]
        num2: list[int] = [j for j in range(1, n + 1) if j % m == 0]
        return sum(num1) - sum(num2)