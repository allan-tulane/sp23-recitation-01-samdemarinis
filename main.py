"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
'''
tabulate is causing errors upon submission

import tabulate
'''
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):

  # if list is empty
  if left > right:
    return -1

  middle = (left + right)//2

  # base case (mid value is the right one)
  if key == mylist[middle]:
    return middle

  # if mid value is greater than right one
  elif mylist[middle] > key:
    return _binary_search(mylist, key, left, middle - 1)

  # if mid value is less than right one
  elif mylist[middle] < key:
    return _binary_search(mylist, key, middle + 1, right)
  """
  description of above^
  
	Recursive implementation of binary search.
  
	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
    

def test_binary_search():
  assert binary_search([1,2,3,4,5], 5,) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 6) == -1
  assert binary_search([1,2,3,4,5], 9) == -1
  assert binary_search([1,2,3,4,5], 2) == 1

def time_search(search_fn, mylist, key):

  t1 = time.time() * 1000
  search_fn(mylist, key)
  t2 = time.time() * 1000
  return t2 - t1

  """
  ^^ description of above
  
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
  

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):

  list_of_lists = []
  list_of_tuples = []
  
  for size in sizes:
    
    list_ = list(range(0, int(size)))
    list_of_lists.append(list_)
  
  for _list in list_of_lists:
    
    t1 = time.time() * 1000
    linear_search(_list, -1)
    t2 = time.time() * 1000
    
    linear_time = t2 - t1

    t3 = time.time() * 1000
    binary_search(_list, -1)
    t4 = time.time() * 1000

    binary_time = t4 - t3

    tuple = (len(_list), linear_time, binary_time)

    list_of_tuples.append(tuple)

  return list_of_tuples
  

          
    
  
  """
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""


def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1