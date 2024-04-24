class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[:]
        expected.sort()
        count: int = 0
        for i, h in enumerate(heights):
            if h != expected[i]:
                count += 1
        return count
            