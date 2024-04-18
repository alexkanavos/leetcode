class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        total_words: list[str] = text.split(' ')
        count: int = len(total_words)
        for word in total_words:
            for char in brokenLetters:
                if char in word:
                    count -= 1
                    break
        if count > 0:
            return count
        else:
            return 0