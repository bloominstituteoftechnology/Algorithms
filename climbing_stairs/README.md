# Climbing Stairs

Imagine a small child ascending a staircase that has `n` steps. The child can hop either 1, 2, or 3 steps at a time. Implement a function `climbing_stairs` that counts the number of possible ways in which the child can ascend the staircase.

For example, for a staircase with `n = 3` (the stair has 3 steps), there are 4 possible ways for the child to ascend the staircase:

1.  They can jump 3 hops of 1 step
2.  They can go up 1 step, followed by a jump of 2 steps
3.  They can jump up 2 steps, then go up the last step
4.  They can make a single jump of 3 steps

Thus, `climbing_stairs(3)` should return an answer of 4.

## Testing

For this problem, there's a test that tests your implementation with small inputs (n <= 10). There's also a separate test that tests your implementation with large inputs (n >= 50).

You'll find that without implementing performance optimizations into your solution, your solution will likely hang on the large input test.

To run the tests separately, run `python test_climbing_stairs.py -k small` in order to run jsut the small input test. Run `python test_climbing_stairs.py -k large` to execute just the large input test. If you want to run both tests, just run `python test_climbing_stairs.py`.

You can also test your implementation manually by executing `python climbing_stairs.py [n]`.

## Hints

- Since this question is asking you to generate a bunch of possible permutations, you'll probably want to use recursion for this.
- Think about base cases that we would want our recursive function to stop recursing on. How many ways are there to climb 0 stairs? What about a negative number of stairs?
- Once we've established some base cases, how can we recursively call our function such that we move towards one or more of these base cases?
- As far as performance optimizations go, caching/memoization might be one avenue we could go down? How should we make a cache available to our recursive function through multiple recursive calls?
