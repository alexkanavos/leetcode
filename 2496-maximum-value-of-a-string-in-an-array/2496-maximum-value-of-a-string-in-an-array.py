class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans: list[int] = []
        for s in strs:
            if s.isnumeric():
                ans.append(int(s))
            else:
                ans.append(len(s))
        return max(ans)