# Stock Prices

prices_arr = [1050, 270, 1540, 2000, 2, 3, 1]


def find_max_profit(prices):
    # Initial variables
    maximum_difference = prices[0]
    minimum_price = prices[0]
    for i in range(len(prices)):
        current_price = prices[i]
        if current_price < minimum_price:
            minimum_price = current_price
        elif (current_price - minimum_price) > maximum_difference:
            maximum_difference = current_price - minimum_price
    return maximum_difference


print(find_max_profit(prices_arr))

# I "think" this algorithm is O(N) due to just one loop for everything.
