class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences: list[int] = [arr.count(num) for num in set(arr)]
        return len(occurrences) == len(set(occurrences))