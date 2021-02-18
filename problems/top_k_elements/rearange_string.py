import heapq

"""
Given a string, find if its letters can be rearranged 
in such a way that no two same characters come next to each other.

Time complexity: O(N * log(N))
Space complexity: O(N)
"""

def rearrange_string(str):
  charFrequencyMap = {}
  for char in str:
    charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all characters to the max heap
  for char, frequency in charFrequencyMap.items():
    heapq.heappush(maxHeap, (-frequency, char))

  # alternate between appending different letters by using a previousChar
  # variable to track which letter you just appended
  previousChar, previousFrequency = None, 0
  resultString = []
  while maxHeap:
    frequency, char = heapq.heappop(maxHeap)
    # add the previous entry back in the heap if its frequency is greater than zero
    if previousChar and -previousFrequency > 0:
      heapq.heappush(maxHeap, (previousFrequency, previousChar))
    # append the current character to the result string and decrement its count
    resultString.append(char)
    previousChar = char
    previousFrequency = frequency+1  # decrement the frequency

  # if we were successful in appending all the characters to the result string, return it
  return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()
