def insertion_sort(arr):
    arr_len = len(arr)

    for index in range(1, arr_len):
        while 0 < index and arr[index] < arr[index - 1]:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index -= 1

    return arr


def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])


def tim_sort(arr):
    runs, sorted_runs = [], []
    arr_len = len(arr)
    new_run = [arr[0]]
    sorted_array = []
    
    for i in range(0, arr_len):
        if arr[i] < arr[i-1]:
            if not new_run:
                runs.append([arr[i-1]])
                new_run.append(arr[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(arr[i])

    for run in runs:
        sorted_runs.append(insertion_sort(run))

    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array

#arr = [5,9,10,3,-4,5,178,92,46,-18,0,7]
arr = [1,5,3,2]
sorted_arr = tim_sort(arr)
print(sorted_arr)
