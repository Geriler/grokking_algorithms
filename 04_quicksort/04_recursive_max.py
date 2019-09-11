def find_max(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        sub_max = find_max(arr[1:])
        if arr[0] > sub_max:
            return arr[0]
        else:
            return sub_max


print(find_max([1, 2, 6, 3, 4, 5]))
