class Solution:
    def fib(self, n: int) -> int:
        fib: list[int] = []
        for i in range(n + 1):
            if i == 0:
                num = 0
            elif i == 1:
                num = 1
            else:
                num: int = fib[i - 1] + fib[i - 2]
            fib.append(num)
        return fib[-1]