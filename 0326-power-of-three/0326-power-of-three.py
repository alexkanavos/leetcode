class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for x in range(20):
            if n == 3 ** x:
                return True
        return False