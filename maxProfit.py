def maxProfit(prices): #O(n^2) brute force
    max_profit = 0

    for i in range(len(prices)):
        curr = i + 1
        while curr < len(prices):
            diff = prices[curr] - prices[i]
            max_profit = max(diff, max_profit)
            curr += 1

    return max_profit

def maxProfitOptimal(prices):
    min_price = float('inf')
    max_price = 0

    for price in prices:
        min_price = min(min_price, price)
        max_price = max(max_price, price - min_price)

    return max_price

def maxProfitMostOptimal(prices):
    min_price = prices[0]
    max_price = 0

    for price in prices:
        if price < min_price:
            min_price = price

        if price - min_price > max_price:
            max_price = price - min_price

    return max_price


prices = [7, 1, 2, 4, 6, 5]
print(maxProfit(prices))
print(maxProfitOptimal(prices))
print(maxProfitMostOptimal(prices))
