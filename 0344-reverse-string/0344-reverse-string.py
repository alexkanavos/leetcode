class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        place: int = -1
        for i in range(len(s)//2):
            s[i], s[place] = s[place], s[i]
            place -= 1
            