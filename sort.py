# compare sort algorithms

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

# test 
test_list = range(100,-1,-1)
print("list: ")
print(test_list)
selectionSort(test_list)
print("list sorted via selection sort algorithms: ")
print(test_list)
