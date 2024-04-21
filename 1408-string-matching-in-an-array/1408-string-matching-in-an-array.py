class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer: set[str] = []
        for word in words:
            for el in words:
                if word != el:
                    if el in word:
                        answer.append(el)
        answer = set(answer)
        return list(answer)