class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1: list[int] = [i for i in set(nums1) if i not in nums2]
        ans2: list[int] = [j for j in set(nums2) if j not in nums1]
        return [ans1, ans2]
        