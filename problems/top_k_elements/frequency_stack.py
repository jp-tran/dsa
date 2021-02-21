import heapq

"""
Design a stack-like data structure with the following operations:
- push(int num): Pushes the number 'num' on the stack.
- pop(): Returns the most frequent number in the stack. If there is a tie, 
  return the number which was pushed later.

Time complexity: O(log(N)) for both push() and pop() methods
Space complexity: O(N)
"""

class Element:
  def __init__(self, num, freq, time):
    self.num = num
    self.freq = freq
    self.time = time

  # methods in heapq will use the __lt__ method to sort the heap's elements
  def __lt__(self, other):
    # sort by higher frequency first
    if self.freq != other.freq:
      return self.freq > other.freq # true means current instance comes before "other"
    # if both have the same frequency, sort by the element that was pushed later
    return self.time > other.time

class FrequencyStack:
  def __init__(self):
    self.max_heap = [] # max heap sorted by frequency
    self.freq_map = {} # maps number to frequency
    self.time = 0

  def push(self, num):
    self.freq_map[num] = self.freq_map.get(num, 0) + 1
    elem = Element(num, self.freq_map[num], self.time)
    heapq.heappush(self.max_heap, elem)
    self.time += 1

  def pop(self):
    num = heapq.heappop(self.max_heap).num
    self.freq_map[num] -= 1
    return num


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()