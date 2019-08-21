"""
Writing programming interview questions hasn't made me rich. Maybe trading Apple stocks will.

Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:

  stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# Returns 6 (buying for $5 and selling for $11)

No "shorting"-you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass)
"""


def get_max_profit(stock_prices_yesterday):
    # brute force approach
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    buy = stock_prices_yesterday[0]
    sell = stock_prices_yesterday[1]

    for i in xrange(0, len(stock_prices_yesterday) - 1):
        buy_price = stock_prices_yesterday[i]
        #max_sell_price = buy_price
        #for j in xrange(i, len(stock_prices_yesterday) - 1):
        #    sell_price = stock_prices_yesterday[j]
        #    max_sell_price = max(max_sell_price, sell_price)
        max_sell_price = max(stock_prices_yesterday[i+1:])
        profit = max_sell_price - buy_price
        if profit > max_profit:
            max_profit = profit
            buy = buy_price
            sell = max_sell_price

    return "(profit: "+str(max_profit)+", buy: "+str(buy)+", sell: "+str(sell)+")"


def get_max_profit_optimized(stock_prices_yesterday):
    # optimized to O(n) time & O(1) space
    # also handle edge cases
    if len(stock_prices_yesterday) < 2:
        raise ValueError("stock prices must have at least 2 prices")

    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    lowest_buy = stock_prices_yesterday[0]
    best_buy = lowest_buy

    for i in xrange(1, len(stock_prices_yesterday) - 1):
        current_price = stock_prices_yesterday[i]
        profit = current_price - lowest_buy
        if profit > max_profit:
            max_profit = profit
            best_buy = lowest_buy

        lowest_buy = min(lowest_buy, current_price)

    return "(profit: "+str(max_profit)+", buy: "+str(best_buy)+", sell: "+str(best_buy+max_profit)+")"


sample_stock1 = [10, 7, 5, 8, 11, 9]                # 6, 5, 11
sample_stock2 = [7, 11, 2, 5, 3, 1, 2]              # 4, 7, 11
sample_stock3 = [25, 23, 24, 20, 22, 17, 18, 5]     # 2, 20, 22
sample_stock4 = [25, 23, 20, 17, 10, 5]             # -2, 25, 23
sample_stock5 = [9]

#print get_max_profit(sample_stock4)
print get_max_profit_optimized(sample_stock5)
