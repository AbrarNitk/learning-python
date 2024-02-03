def minimum(arr, start_from):
    # this function takes the array and gives back the minimum element
    min = 9999999
    min_index = 0
    for index in range(start_from, len(arr)):
        if arr[index] < min:
            min = arr[index]
            min_index = index
    return min_index


def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


# this function takes an array and sort it in-place
def sort(arr):
    for i in range(0, len(arr)):
        # arr = [4, 5, 1, 3, 2]
        # min = 1
        # arr = [1, 5, 4, 3, 2]
        min_index = minimum(arr, i)
        swap(arr, i, min_index)


def main():
    arr = [4, 5, 1, 3, 2]
    sort(arr)
    print(arr)


if __name__ == '__main__':
    main()

print("hello")