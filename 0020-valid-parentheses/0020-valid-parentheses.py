class Solution:
    def isValid(self, s: str) -> bool:
        m = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in m.values():
                stack.append(char)
            elif char in m.keys():
                if not stack or m[char] != stack.pop():
                    return False
            else:
                return False
        return not stack
        