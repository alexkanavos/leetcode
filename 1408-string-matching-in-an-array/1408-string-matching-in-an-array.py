class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = set([])
        for word in words:
            for el in words:
                if word != el:
                    if el in word:
                        answer.add(el)
        # answer = set(answer)
        return list(answer)