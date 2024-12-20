def sum_of_differences(arr):
    arr.sort(reverse = True)
    diff = 0
    for i in range(len(arr) - 1):
        diff += arr[i] - arr[i + 1]
    return diff
