def multiple_of_index(arr):
    new = []
    for i in range(len(arr)):
        if arr[i] == 0: new.append(0)
        elif i != 0 and arr[i] % i == 0: new.append(arr[i])
    return new
