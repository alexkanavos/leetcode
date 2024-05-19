class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        reversed1: str = str(num)[::-1]
        while reversed1.startswith('0'):
            reversed1 = reversed1[1::]
        reversed2: str = reversed1[::-1]
        return reversed2 == str(num)