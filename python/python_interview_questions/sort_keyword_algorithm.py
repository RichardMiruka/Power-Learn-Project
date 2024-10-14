# sort without using sort keyword

def sort_without_sort_keyword(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    arr = [5, 2, 8, 1, 4, 7, 6, 3]
    print(sort_without_sort_keyword(arr)) # [1, 2, 3, 4, 5, 6, 7, 8]

