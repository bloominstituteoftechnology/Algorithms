# Stock Prices

You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 

Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

## Testing

Run the test file by executing `python test_stock_prices.py`.

You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

## Hints

 * For this problem, we essentially want to find the difference between the smallest and largest prices in the list of prices.

 ##Solution
 My solution here works, but the test keeps returning None for profit. It seems to want to use find_max_profit(args.integers) to store the solution, but I couldn't find a way to do so.  In terms of runtime complexity, it scales linearly; each input has it run another two checks.