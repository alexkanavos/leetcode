class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        amounts: list[int] = [sum(el) for el in accounts]
        return max(amounts)