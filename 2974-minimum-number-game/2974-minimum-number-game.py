class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr: list[int] = []
        while nums != []:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            arr.append(bob)
            arr.append(alice)
        return arr