class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters: list[chr] = []
        for char in s:
            letters.append(char)
            if letters.count(char) > 1:
                return char