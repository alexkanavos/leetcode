class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        initial_number = [str(d) for d in digits]
        initial_number = int(''.join(initial_number))
        new_number = str(initial_number + 1)
        result = [int(el) for el in new_number]
        return result