from collections import deque

"""
BFS-like approach to generating permutations
Generates each "node" by inserting at different positions

Time complexity: O(N ∗ N!)
There are N! permutations. At each iteration, we insert a new number in each of the
current permutations, which take O(N) time.

Space complexity: O(N ∗ N!)
There are N! permutations, each containing N elements.
"""

def find_permutations(nums):
  numsLength = len(nums)
  result = []
  permutations = deque() 
  permutations.append([]) # initialize queue with root node

  for currentNumber in nums:
    # we will take all existing permutations and add the current number to create new permutations
    n = len(permutations) # get size of current level
    for _ in range(n): # iterate through all nodes at current level
      oldPermutation = permutations.popleft()
      # create a new permutation by adding the current number at every position
      
      for j in range(len(oldPermutation)+1):
        newPermutation = list(oldPermutation)
        newPermutation.insert(j, currentNumber)

        # decide if we should append current node's children to queue
        if len(newPermutation) == numsLength:
          result.append(newPermutation)
        else:
          permutations.append(newPermutation)

  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
