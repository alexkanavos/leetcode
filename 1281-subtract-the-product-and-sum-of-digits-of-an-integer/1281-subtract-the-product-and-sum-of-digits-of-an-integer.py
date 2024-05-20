class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n: list[int] = [int(c) for c in str(n)]
        product_dig: int = 1
        for i in n:
            product_dig *= i
        return product_dig - sum(n)