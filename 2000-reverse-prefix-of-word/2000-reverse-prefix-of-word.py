class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            index: int = word.index(ch) + 1
            word: list[chr] = list(word)
            word = word[:index:][::-1] + word[index::]
            return ''.join(word)
        else:
            return word
        