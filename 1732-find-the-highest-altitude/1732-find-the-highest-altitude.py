class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans: list[int] = [0]
        for i in range(len(gain)):
            ans.append(ans[-1] + gain[i])
        return max(ans)