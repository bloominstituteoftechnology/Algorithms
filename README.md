# Algorithms

Now that we've talked about some strategies for solving algorithmic problems and walked through some examples, it's time to practice applying those strategies!

To quickly recap, when you're confronted with a problem you haven't encountered before, the general strategy is as follows:

1. Understand the question you're being asked. The way everyone will go about doing this may be slightly different, but in general, a couple of good ways to do this are:
   * Ask clarifying questions to understand the ins and outs of the problem.
   * Based on the problem description, think about some edge cases that may be relevant to the problem. If it isn't clear how those edges cases should be handled by your implementation, ask what the expectations are for that particular edge case.

2. Scribble stuff down. This really helps you to keep track of everything that needs to be handled by your solution. 
   * It is also often helpful to draw out a diagram or list out the steps of how you expect the problem should be solved. This helps you clarify how the solution needs to work, and will oftentimes also clue you in on edge cases you might not have thought of.

 3. Come up with a first pass idea as to how to tackle the problem. It doesn't matter if it's a "bad" idea. At this point, we just need somewhere to start. 
    * Whatever first comes to your mind when looking at the problem in front of you, run with it if you don't have any better ideas. Iteration and improvement of your implementation comes afterwards.
    * If you have multiple ideas, _write them all down_, then decide which one you want to go with initially.
    * Once you've implemented a solution, think about what your implementation will output given some test inputs. Does it handle all the expected edge cases? Maybe it does and maybe it doesn't. If it doesn't, we'll come back to improve upon it later. 

 4. Now that we have a first pass implementation, it's time to think about how we can improve upon it.
    * Figure out the runtime and space complexity of your first-pass implementation.
    * What is it about your first-pass implementation that causes the runtime or space complexity to suffer? 
    * Think about some ways in which we can improve it. For example, can we utilize memoization?

 5. Implement an improved solution to the problem using the idea(s) you came up with from step 4. 

Please don't consider this list of steps to be canonical or definitive. Everyone thinks about problems differently. Treat them only as guidelines. 

As you accrue more experience solving these sorts of algorithmic problems, you'll start to encounter problems you'll have seen before, i.e., some problems won't be novel to you anymore. In those cases you'll oftentimes be able to implement a better solution right off the bat, i.e., you'll be able to skip step 3. 

## What You'll Be Doing

The contents of this sprint are all about giving you the opportunity to practice applying the guidelines that were introduced. 

Each directory contains a separate problem that you'll be tasked with solving. Inside each directory, you'll find instructions for that problem, along with a test file as well as an empty skeleton file. 

There isn't an official prescribed order for tackling the problems, though a subjective ranking of the given problems from easiest to hardest might go something like this:

 1. `stock_prices`
 2. `recipe_batches`
 3. `counting_stairs`
 4. `rock_paper_scissors`
 5. `making_change`
 6. [Stretch Problem] `knapsack`

For each problem, `cd` into the directory, read the instructions for the problem, implement your solution in the skeleton file, then test it using the provided test file. 

The later problems definitely get progressively more difficult, especially when it comes to deriving a more performant solution. Don't feel bad if you aren't able to figure them out within the timeframe of the sprint. Again, always remember that so long as you put in an earnest effort into attempting to solve these problems, you're learning and getting better. Getting the 'right answer' is just the proverbial cherry on top of the sundae. 