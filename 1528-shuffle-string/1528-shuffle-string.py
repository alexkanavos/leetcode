class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        p: int = 0
        ans: list[chr] = list(s)
        for i in indices:
            ans[i] = s[p]
            p += 1
        return ''.join(ans)
            