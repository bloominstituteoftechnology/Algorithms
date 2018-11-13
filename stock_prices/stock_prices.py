# Stock Prices

prices_arr = [1050, 270, 1540, 2000, 2, 3, 1]
prices_arr2 = [100, 90, 80, 50, 20, 10]


def find_max_profit(prices):
    # Initial variables
    minimum_price = prices[0]
    maximum_difference = prices[1] - minimum_price
    for i in range(1, len(prices)):
        current_price = prices[i]
        if current_price < minimum_price:
            minimum_price = current_price
        elif (current_price - minimum_price) > maximum_difference:
            maximum_difference = current_price - minimum_price
    return maximum_difference
    # O(n^2)
    # max_profit = 0
    # for i in range(len(prices)):
    #     for j in range(i):
    #         max_profit = max(max_profit, prices[i] - prices[j])
    # return max_profit


print(find_max_profit(prices_arr2))

# I "think" this algorithm is O(N) due to just one loop for everything.
