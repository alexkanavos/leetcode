class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sentence: list[str] = s.split()
        sentence: list[str] = sentence[:k:]
        ans: str = ' '.join(sentence)
        return ans