# Making Change

You work as a bank teller, handling people's bank transactions (this is your part-time gig while you're studying at Lambda; only fourteen more weeks of this stinking job until you go find a job as a software developer!). 

One day one of the wealthiest and also most eccentric patrons of the bank walks up to your stall. He hands you some cash and tells you he wants you to figure out exactly how many ways there are to make change for the amount of money he plopped down in front of you using pennies, nickels, dimes, quarters, and half-dollars. 

Since this is a bank, you basically have an infinite supply of coinange. Write a function `making_change` that receives as input an amount of money in cents as well as an array of coin denominations and calculates the total number of ways in which change can be made for the input amount using the given coin denominations. 

For example, `making_change(10)` should return 4, since there are 4 ways to make change for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:

 1. We can make change for 10 cents using 10 pennies
 2. We can use 5 pennies and a nickel
 3. We can use 2 nickels
 4. We can use a single dime

## Testing 

For this problem, there's a test that tests your implementation with small inputs (amounts of change up to 300 cents). There's also a separate test that tests your implementation with large inputs (amounts of change >= 350 cents). 

You'll find that without implementing performance optimizations into your solution, your solution will likely hang on the large input test. 

To run the tests separately, run `python test_making_change.py -k small` in order to run jsut the small input test. Run `python test_making_change.py -k large` to execute just the large input test. If you want to run both tests, just run `python test_making_change.py`.

## Hints

 * This problem can be thought of as a more difficult version of the climbing stairs problem. 
 * As far as base cases go, again, think about some cases where we'd want the recursion to stop executing. What should happen when the amount of cents given is 0? What should happen when the amount of cents given is negative? What about when we've used up all of the available coin denominations?
 * As far as performance optimizations go, caching/memoization might be one avenue we could go down? How should we make a cache available to our recursive function through multiple recursive calls?