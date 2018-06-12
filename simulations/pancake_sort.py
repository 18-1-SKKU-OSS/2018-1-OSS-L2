def pancake_sort(arr, simulation = False):
    """
    Pancake_sort
    Sorting a given array
    mutation of selection sort

    reference: https://www.geeksforgeeks.org/pancake-sorting/
    
    Overall time complexity : O(N^2)
    """
    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)
    
    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    for cur in range(len(arr), 1, -1):
        #Finding index of maximum number in arr
        index_max = arr.index(max(arr[0:cur]))
        if index_max+1 != cur:
            #Needs moving
            if index_max != 0:
                #reverse from 0 to index_max
                arr[:index_max+1] = reversed(arr[:index_max+1])
            # Reverse list
            arr[:cur] = reversed(arr[:cur])
            
        if simulation:
            iteration = iteration + 1
            print("itertaion", iteration,":",*arr)
    return arr

