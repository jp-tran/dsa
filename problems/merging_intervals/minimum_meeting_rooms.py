"""
Given a list of intervals representing the start and end time of 'n' meetings, 
find the minimum number of rooms required to hold all the meetings.

Time complexity: O(n*log(n))
    - sorting takes O(n*log(n))
    - iterating through sorted meetings, we may do up to 
    two log(n) operations per meeting
Space complexity: O(n)
    - sorting takes O(n)
    - min heap may grow to size O(n)
"""

import heapq

class Meeting:
  def __init__(self, start, end):
    self.start = start
    self.end = end
  
  def __lt__(self, other):
    return self.end < other.end

def min_meeting_rooms(meetings):
  if not meetings:
    return 0

  # sort by meeting start time
  meetings.sort(key=lambda x: x.start)

  # the min number of rooms required is the max number of rooms used
  # at any given time
  num_rooms = 0

  # maintain a min heap sorted by meeting end time
  # size of min heap at any given time will be the number of meetings
  # happening at that time
  min_heap = []
  
  for i in range(len(meetings)):
    meeting = meetings[i]
    while min_heap and min_heap[0].end <= meeting.start:
      heapq.heappop(min_heap)
    heapq.heappush(min_heap, meeting)
    num_rooms = max(num_rooms, len(min_heap))
  
  return num_rooms

def main():
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))) # prints 2
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]))) # prints 2 
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]))) # prints 1
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]))) # prints 2
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))) # prints 2


main()
