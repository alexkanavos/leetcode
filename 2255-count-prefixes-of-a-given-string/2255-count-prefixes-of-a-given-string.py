class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count: int = 0
        for el in words:
            if s.startswith(el):
                count += 1
        return count