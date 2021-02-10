def search_bitonic_array(arr, key):
  # find the peak index
  lo = 0
  hi = len(arr) - 1
  while (lo < hi):
    mid = (hi + lo) // 2
    is_increasing = arr[mid] < arr[mid+1]
    if is_increasing:
      # mid can never be the peak when is_increasing, so we can safely set low = mid +1
      lo = mid + 1 
    else:
      hi = mid
  
  peak_idx = lo

  # binary search for key in left half
  left_search_result = binary_search(arr, 0, peak_idx, key, True)
  if left_search_result != -1:
    return left_search_result

  # binary search for key in right half
  right_search_result = binary_search(arr, peak_idx+1, len(arr)-1, key, False)
  if right_search_result != -1:
    return right_search_result

  return -1

def binary_search(arr, lo, hi, key, is_increasing):
  while (lo <= hi):
    mid = (hi + lo) // 2
    if arr[mid] == key:
      return mid
    elif (is_increasing and key < arr[mid]) or (not is_increasing and key > arr[mid]):
      hi = mid - 1
    else:
      lo = mid + 1
  return -1

def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()
