class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j] == 0:
                    nums1[j] = nums2[i]
                    break
        nums1 = nums1.sort()
        