class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lengths: list[list[str]] = [len(el.split()) for el in sentences]
        return max(lengths)