from typing import List


def maxProfit(prices: List[int]) -> int:
        buy = prices[0]
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > maxprofit:
                maxprofit = prices[i] - buy

        return maxprofit

print(maxProfit([2,1,2,0,1]))