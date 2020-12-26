 class Solution:
   def mergeSort(self, nums, l, r):
      if l == r:
          return [nums[l]]
      mid = (l + r) // 2
      left = self.mergeSort(nums, l, mid)
      right = self.mergeSort(nums, mid+1, r)
      return self.merge(left, right)
  
  def merge(self, left, right):
      result = []
      l = r = 0
      while l < len(left) and r < len(right):
          if self.compare(left[l], right[r]):
              result.append(left[l])
              l += 1
          else:
              result.append(right[r])
              r += 1
      result.extend(left[l:] or right[r:])
      return result
  
  def compare(self, n1, n2):
    # comparator function used in LC problem 179: Largest Number
    # e.g. return true if n1 = '34' and n2 = '3'
      return str(n1) + str(n2) > str(n2) + str(n1)