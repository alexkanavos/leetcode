class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        diff: list[int] = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        min_diff: int = min(diff)
        indices: list[int] = [i for i, el in enumerate(diff) if el == min_diff]
        ans: list[list[int]] = [[arr[i], arr[i+1]] for i in indices]
        return ans