class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        position: int = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[position] = nums[position], nums[i]
                position += 1
        return nums