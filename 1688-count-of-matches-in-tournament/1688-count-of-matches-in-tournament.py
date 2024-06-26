class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches: int = 0
        while n > 1:
            if n % 2 == 0:
                matches += n / 2
                n = n / 2
            else:
                matches += (n - 1) / 2
                n = (n + 1) / 2
        return int(matches)