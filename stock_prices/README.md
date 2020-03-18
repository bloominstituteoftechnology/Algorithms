# Stock Prices

You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock.

Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

list_of_stock_prices = [amazon]

def find_max_profit(list_of_stock_prices):
#find the greatest difference between prices 1 and 2, where price 1 has an earlier index than 2 # need a max profit array
arr_max_profit = []
#price 1 will exclude the last in the list
arr_price_1 = list_of_stock_prices[0: len(list_of_stock_prices) - 1]

            #sort these to make iteration easier? yes, but COPY the array first because we need the original intake to check for indices later. SCRATCH THAT actually just use the input for figuring out relative indices

            <!-- sorted_price_1 = arr_price_1.copy() #because the value of array_price_1 is just a reference to memory, not the value itself (here we copy the value)
            sorted_price_1.sort() -->


        #price 2 will exclude the first in the list,
            arr_price_2 = list_of_stock_prices[1:]

            #sort these to make iteration easier
            arr_price_2.sort()

        #find the highest number first for price 2
        # set that number as the highest number
            i_list_price = 0
            i_price_2 = len(list_of_stock_prices)-2
            highest_stock_sell = arr_price_2[i_price_2] #should this go here or in the for loop? does it matter?

            #now find the lowest number that comes before that and set that as price 1
        for i_list_price in range(0, len(list_of_stock_prices)):
            if i_list_price < list_of_stock_prices.index(highest_stock_sell):
                price_1 = arr_price_1[i_list_price]
                price_2 = highest_stock_sell
                arr_max_profit.append(price_2 - price_1)
                #i_list_price += 1 this is unnecessary because using for loop
            elif i_price_2 >= 1:
                i_price_2 -= 1
                i_list_price = 0 #reset it back to 0 for next highest number
            else:
                return
            #subtract price 1 from price 2, append the value to an array called profits
        #iterate for the next highest number
            # set that number as the highest number
            #now find the lowest number that comes before that and set that as price 1
            #subtract price 1 from price 2, append the value to an array called profits
        #when done with iterations through sorted_price_2 array return profits array
        #sort profits array from smallest to greatest and return the value at the last index as the max profit
        arr_max_profit.sort()

        return arr_max_profit[-1]

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices.

## Testing

Run the test file by executing `python test_stock_prices.py`.

You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

## Hints

For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices.

So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`?
