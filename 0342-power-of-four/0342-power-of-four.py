class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for x in range(20):
            if n == 4 ** x:
                return True
        return False