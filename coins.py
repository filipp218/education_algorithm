https://leetcode.com/problems/coin-change/submissions/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount + 1):
            cur = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    if result[i - coin] < cur:
                        cur = result[i - coin] + 1
            result[i] = cur
        return -1 if result[-1] == float('inf') else result[-1]
