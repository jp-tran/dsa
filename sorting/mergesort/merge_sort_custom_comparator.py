 class Solution:
   def mergeSort(self, nums):
      if len(nums) <= 1:
          return
      mid = len(nums) // 2
      left = nums[:mid]
      right = nums[mid:]
      self.mergeSort(left)
      self.mergeSort(right)
      self.merge(nums, left, right)
  
  def merge(self, nums, left, right):
      l = r = k = 0
      while l < len(left) and r < len(right):
          if self.compare(left[l], right[r]):
              nums[k] = left[l]
              l += 1
          else:
              nums[k] = right[r]
              r += 1
          k += 1
      
      while l < len(left):
          nums[k] = left[l]
          l += 1
          k += 1
      
      while r < len(right):
          nums[k] = right[r]
          r += 1
          k += 1

  
  def compare(self, n1, n2):
    # comparator function used in LC problem 179: Largest Number
    # e.g. return true if n1 = '34' and n2 = '3'
      return str(n1) + str(n2) > str(n2) + str(n1)