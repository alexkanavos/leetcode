class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans: list[int] = []
        for el2 in arr2:
            if arr1.count(el2) != 0:
                ans += arr1.count(el2) * [el2]
                arr1 = [i for i in arr1 if i != el2]
        arr1.sort()
        return ans + arr1