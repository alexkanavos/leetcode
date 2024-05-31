class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans: int = 0
        for c in s:
            ans += abs(s.index(c) - t.index(c))
        return ans
        