""" Standard Binary Search """
def binary_search(nums: List[int], target: int) -> int:
  l = 0
  r = len(nums) - 1
  while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
      return mid
    elif target < nums[mid]:
      r = mid - 1
    elif nums[mid] < target:
      l = mid + 1
  return -1

""" Binary Search for a Range of Numbers """
class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    # binary search for target
    def bs(nums, target, searching_left):
      l = 0
      r = len(nums) # allows while loop to run even if array only has one entry
      # we want to run loop to put r past its actual position
      # outside the function we always subtract 1 from r
      while l < r:
        mid = (l + r) // 2
        if nums[mid] > target or (searching_left and nums[mid] == target):
          r = mid
        else:
          l = mid + 1 # need to add 1 because mid value is floored (without +1 we could be stuck in inf loop)
      return l
    
    if not nums:
      return [-1, -1]
    
    #search for leftmost/starting position
    starting = bs(nums, target, True)
    
    #check that leftmost index is our target
    if starting == len(nums) or nums[starting] != target:
      return [-1, -1]
    
    #search for rightmost/ending position
    ending = bs(nums, target, False) - 1
    
    return [starting, ending]