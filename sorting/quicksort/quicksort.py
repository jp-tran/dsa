# quicksort algorithm
import random
import copy

# returns random index in the array segment
# left: left index of array segment
# right: right index of array segment
def choose_pivot(left, right):
    return random.randint(left, right)


# partitions so that all values less than pivot are placed to the left of pivot
# and all values greater than pivot are placed to the right of pivot
# returns index of pivot once arr has been partitioned
# arr: original array to partition
# left: left index bounding segment to partition
# right: right index bounding segment to partition
# pivot: index of pivot
def partition(arr, left, right, pivot):
    arr[left], arr[pivot] = arr[pivot], arr[left] #swap pivot with leftmost element
    pivot_val = arr[left]
    i = left + 1 #index of leftmost element greater than the pivot value
    for j in range(left + 1, right + 1):
        if arr[j] < pivot_val:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
    arr[left], arr[i-1] = arr[i-1], arr[left] #swap pivot to correct position
    return i-1


# implementation of quicksort algorithm
# arr: array to be sorted
# left: left index of array segment to be sorted
# right: right index of array segment to be sorted
def quicksort(arr, left, right):
    global TOTAL_COMP
    TOTAL_COMP += (right - left) #keep track of number of comparisons
    if left >= right:
        return
    pivot = choose_pivot(left, right) #index of randomly chosen pivot
    pivot = partition(arr, left, right, pivot) #index of chosen pivot after partition
    quicksort(arr, left, pivot - 1)
    quicksort(arr, pivot + 1, right)


def compare_sort_funcs(quicksort_arr, python_sort_arr):
    # flag = True
    # incorrect = []
    # for index, num in enumerate(quicksort_arr):
    #     if index+1 != num:
    #         flag = False
    #         incorrect.append([index, num])
    # print("Both arrays are the same: ", flag)
    # print("Incorrect locations:")
    # print(incorrect)
    print("Both arrays are the same: " + str(quicksort_arr == python_sort_arr))

if __name__ == '__main__':
    TOTAL_COMP = 0 #running total of comparisons for a way of choosing the pivot

    with open('quick_sort_test_data.txt', 'r') as f:
        orig_array = [int(num.strip()) for num in f]
    
    print(orig_array[0])
    arr1 = copy.deepcopy(orig_array)
    n = len(arr1)
    quicksort(arr1, 0, n-1)

    with open('quick_sort_test_output.txt', 'w') as output_f:
        for num in arr1:
            output_f.write(f'{num}\n')

    # compare quicksort and python's sort function
    compare_sort_funcs(arr1, sorted(orig_array))

    print('Total number of comparisons: ', TOTAL_COMP)