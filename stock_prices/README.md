# Stock Prices

You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 

Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

## Testing

Run the test file by executing `python test_stock_prices.py`.

You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

## Hints

 * For this problem, we essentially want to find the difference between the smallest and largest prices in the list of prices.


 braindump notes:

 Find the biggest gap in prices in the future

create a list of prices in the future

If time > current time
	add to list

for each in list - others in list ro find the biggest gap

lownum list defined
highnum list defined

For price in list
	if price - [i] = positive number 
		add to lownum <— new  
  elif price - [i] = negative number
    add to highnum

what if you append into a list.... then find the biggest gap by finding the biggest gap per price.... put into a new list..... then find the biggest number out of the collection of largest numbers?

