from typing import *
from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        setOfStones = set(stones)

        @lru_cache(None)
        def canJump(stonePosition, jumpUnits):
            if jumpUnits <= 0 or stonePosition not in setOfStones:
                return False
            if stonePosition == target:
                return True
            # Try the three possible jumps with k-1, k and k+1 units from
            # the current stone.
            return (canJump(stonePosition + jumpUnits - 1, jumpUnits - 1) or
                    canJump(stonePosition + jumpUnits, jumpUnits) or
                    canJump(stonePosition + jumpUnits + 1, jumpUnits + 1))
        return canJump(1, 1)
        
