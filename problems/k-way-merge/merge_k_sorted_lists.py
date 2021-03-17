from __future__ import print_function
import heapq

"""
Given an array of 'K' sorted LinkedLists, merge them into one sorted list.

Time complexity: O(N * log(K)), where N is the total number of elements
and K is the number of lists

Space complexity: O(K) for min-heap
"""

class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  # used by heapq to compare two nodes
  def __lt__(self, other):
    return self.value < other.value


def merge_lists(lists):
  resultHead = ListNode(0)

  min_heap = [head for head in lists] # assume all head nodes are valid nodes
  heapq.heapify(min_heap)
  curr = resultHead

  while min_heap:
    smallest = heapq.heappop(min_heap) # pop the smallest node
    if smallest.next:
      # heap push next node from the same list as the one that was popped
      heapq.heappush(min_heap, smallest.next)
    curr.next = smallest
    curr = curr.next

  return resultHead.next


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()