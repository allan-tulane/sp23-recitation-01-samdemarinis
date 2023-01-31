# CMPS 2200  Recitation 01

**Name (Team Member 1):** Sam DeMarinis 
**Name (Team Member 2):** Zoe Oboler

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment. 
- Click on your personal github repository for the assignment.
- Login in Repls https://replit.com/repls and then create a new replit by importing from github repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.
- Make sure the dependencies are installed. Please use 'pip install -r requirements.txt'.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

The worst case input value of 'key' for 'linear_search' would be a value that either does not appear in the list at all or one that appears at the end of the list. This is due to the fact that 'linear_search' iterates over each element in the list to see if it matches the key. If the key does not exist in the list or if it is the last element, 'linear_search' must iterate over every single element in the list. This results in a work of O(n) for the worst case scenario. For 'binary_search', the worst case input value would be a value that either does not appear in the list at all or one that appears as the first or last element of the list. This is due to the fact that the algorithm repeatedly checks the middle element of the list to see if it matches the key, and it has to do the most operations if the desired value is at the far left or far right of the list.

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

The best case input value of 'key' for 'linear_search' would be the value that exists in the first position of the list. Since 'linear_search' iterates through each element of the list to see if they match the 'key', the best case would be for there to only be one iteration. This happens when the function only needs to look at the first element. The best case input value of 'key' for 'binary_search' would be the value that exists in the middle of the list. This is due to the fact that this function recursively examines the middle value of the list to see if they 'key' is higher or lower. If the middle value happens to be the right 'key' value, then the algorithm can stop because it found the right spot.

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:
|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.013 |    0.012 |
|      100 |    0.011 |    0.006 |
|     1000 |    0.089 |    0.011 |
|    10000 |    0.915 |    0.019 |
|   100000 |    9.962 |    0.028 |
|  1000000 |  177.721 |    0.054 |
| 10000000 | 1921.761 |    0.044 |
**TODO: add your timing results here**

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

Our results generally match the theoretical running times. If we were to plot the points on a graph it would be somewhat close to the original functions. For instance the linear function increases by about 10 times each time n is multiplied by 10. However, due to these functions relying on the worst case runtime there is some deviation. If the key is placed earlier in the list (or closer to the center in the case of binary search) the runtime will be shorter than the expected worst case runtime. For instance for the binary search when n = 10000000 the running time is actually shorter than when n = 1000000. We see the same phenomonon when n = 10 and 100. 
**TODO: your answer goes here**

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search?
      + O(kn)
  + For binary search? **TODO: your answer goes here**
      + Theta(n^2) + k*O(log_2(n)) = O(n^2)
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting?  **TODO: your answer goes here**
      +  It is only necessary to sort the list once. If n is really large and k is really small, then sorting the list takes a long time and linear search is more efficient. However, when n is small and k is large, binary search is always more efficient. When k > n, it is more efficient to sort and then perform binary search