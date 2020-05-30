# compare sort algorithms
# import packages
from time import time
# selection sort
def selectionSort(target_list):
    """Takes a list as an input and sorts it using selection sort algorihtm

    Args:
        target_list (list): a list of ordered objects

    Returns:
        no returns

    Time complexity:
        O(n^2)
    """
    l = len(target_list)
    for i in range(l):
        for j in range(i+1,l):
            if target_list[i] > target_list[j]:
                temp = target_list[i]
                target_list[i] = target_list[j]
                target_list[j] = temp

# test function
def test_sort_algorithm(function, test_list = range(10,-1,-1), verbose = False):
    """Tests a selection sort algorihtm and returns the time

    Args:
        function: the sort algorihtm which we want to test
        test_list (list): a list which will be used for testing
        verbose (bool): prints information to the screen depending on its value
            if verbose = True prints list before and after sort

    Returns:
        sort_time = time spent to sort

    Time complexity:
        time complexity of function algortim
    """

    test_list = test_list
    if verbose:
        print(" ===> list before sort: ")
        print(test_list)
    tic = time()
    function(test_list)
    toc = time()
    if verbose:
        print("list sorted via selection sort algorithms: ")
        print(test_list)

    sort_time = (toc - tic)
    return sort_time

# dictionary of algorithm
algorithms = dict()
algorithms["selection sort"] = (selectionSort, {})

# test sort algortims
n = [10,100,1000,2000]
for i in n:
    for _ , (algorithm_func , sort_times) in algorithms.items():
        test_list = range(i,-1,-1)
        sort_time = test_sort_algorithm(algorithm_func, test_list)
        sort_times[i] = sort_time

print(algorithms.values())
