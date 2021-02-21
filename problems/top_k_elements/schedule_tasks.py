from collections import Counter, deque
import heapq

"""
You are given a list of tasks that need to be run, in any order, on a server. 
Each task will take one CPU interval to execute but once a task has finished, 
it has a cooling period during which it can’t be run again. If the cooling period 
for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the 
server needs to finish all tasks.

Time complexity: O(N*log(N) + N*k)
Space complexity: O(N)
"""

def schedule_tasks(tasks, k):
  num_tasks_remaining = len(tasks)

  # count the number of times each task occurs
  task_counts = Counter(tasks)

  # put all tasks and their associated counts into a max heap
  max_heap = []

  for task, freq in task_counts.items():
    heapq.heappush(max_heap, (-freq, task))

  # process tasks
  num_intervals = 0
  queue = deque()

  while num_tasks_remaining > 0:
    num_intervals += 1

    if max_heap:
      freq, task = heapq.heappop(max_heap) # O(log(N)) operation
      freq += 1
      num_tasks_remaining -= 1
    else:
      freq, task = 1, 'idle'
    
    queue.append((freq, task))

    if len(queue) == k + 1:
      next_task = queue.popleft()
      if next_task[0] < 0:
        heapq.heappush(max_heap, next_task)
    
  return num_intervals


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()

