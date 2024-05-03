class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stone_1: int = max(stones)
            stones.remove(stone_1)
            stone_2: int = max(stones)
            stones.remove(stone_2)
            if stone_1 != stone_2:
                stones.append(abs(stone_1 - stone_2))
        if stones:
            return stones[0]
        else:
            return 0