class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = [c for c in str(x)]
        reverse = [digit for digit in num[-1::-1]]
        if num == reverse:
            return True