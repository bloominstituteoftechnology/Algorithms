# Stock Prices

prices_arr = [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):
    # Initial variables
    min_stock = prices[0]
    min_index = prices[0]
    max_stock = prices[0]
    max_index = prices[0]

    # Loop through array
    for ind, num in enumerate(prices):
        # Inner for loop to compare every value...
        for ind2, num2 in enumerate(prices):
            # Go through inner for loop
            if ind2 < ind:
                # Check if current number is less than minimum stock value and ensure that the index on the outer
                # loop is greater than the current minimum index, I'm treating the index as a point in time.
                if num < min_stock and ind < min_index:
                    min_stock = num
                    min_index = ind
                # Do the same as above only for the max numbers
                elif num > max_stock and ind < max_index:
                    max_stock = num
                    max_index = ind
                # Compare inner for loop current num against minimum stock
                elif num2 < min_stock:
                    min_stock = num2
                    min_index = ind
                # Compare inner for loop current num against maximum stock
                elif num2 > num:
                    max_stock = num2
                    max_index = ind2
    return max_stock - min_stock


print(find_max_profit(prices_arr))

# I "think" this algorithm is O(N2) due to just one inner for loop
