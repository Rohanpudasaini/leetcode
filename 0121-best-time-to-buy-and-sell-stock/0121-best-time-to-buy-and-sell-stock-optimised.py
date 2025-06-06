class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_price = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > buy:
        #             current_profit = prices[j] - buy
        #             if current_profit > max_price:
        #                 max_price = current_profit
        # return max_price

        # maxPro = 0
        # n = len(prices)


        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if prices[j] > prices[i]:
        #             maxPro = max(prices[j] - prices[i], maxPro)


        # return maxPro

        max_profit = 0
        minimum = 999999
        for price in prices:
            if price < minimum:
                minimum = price
            max_profit = max(price - minimum, max_profit)
        return max_profit


            
        