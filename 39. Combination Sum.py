class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for c in candidates:
            for i in range(1, target + 1):
                if i == c:
                    dp[i].append([c])
                elif i - c > 0:
                    dp[i] += [s + [c] for s in dp[i - c]]
        return dp[target]
        
