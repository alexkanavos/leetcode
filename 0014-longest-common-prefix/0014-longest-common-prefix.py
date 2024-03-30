class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)
        while True:
            check_list = [word.startswith(shortest_word) for word in strs]
            if all(check_list):
                return shortest_word
            else:
                shortest_word = shortest_word[:-1:]
        