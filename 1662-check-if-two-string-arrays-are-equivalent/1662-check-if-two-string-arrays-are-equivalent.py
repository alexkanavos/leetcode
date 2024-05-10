class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        conc1: str = ''
        conc2: str = ''
        for element in word1:
            conc1 += element
        for element in word2:
            conc2 += element
        return conc1 == conc2