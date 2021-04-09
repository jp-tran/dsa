"""
For 'K' employees, we are given a list of intervals representing each employee’s working hours. 
Our goal is to determine if there is a free interval which is common to all employees. 
You can assume that each list of employee working hours is sorted on the start time.

Time complexity: O(n*log(k))
    where n is the total number of intervals, and k is the total number of employees

Space complexity: O(n)
    note that this could be improved to O(k) by appending to results inside of the while loop
"""


from __future__ import print_function
import heapq

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

    def __lt__(self, other):
        if self.start < other.start:
            return True
        else:
            return False

class EmployeeInterval:
    def __init__(self, interval, employee_idx, interval_idx):
        self.interval = interval
        self.employee_idx = employee_idx
        self.interval_idx = interval_idx
    
    def __lt__(self, other):
        return self.interval.start < other.interval.start

def find_employee_free_time(schedule):
    result = []

    # k-way merge 
    intervals = []
    heap = []

    # initialize heap
    for employee_idx, times in enumerate(schedule):
        heap.append(EmployeeInterval(times[0], employee_idx, 0))
    
    heapq.heapify(heap)

    # add all heap items to the intervals list, sorted by start time
    while heap:
        employee_interval = heapq.heappop(heap)
        intervals.append(employee_interval.interval)

        employee_idx = employee_interval.employee_idx
        interval_idx = employee_interval.interval_idx
        work_times = schedule[employee_idx]
        if interval_idx + 1 < len(work_times):
            nxt = EmployeeInterval(work_times[interval_idx + 1], employee_idx, interval_idx + 1)
            heapq.heappush(heap, nxt)

    # determine free intervals (to save memory, this could be done inside the while loop above)
    prev_end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= prev_end:
            prev_end = max(prev_end, interval.end)
        else:
            result.append(Interval(prev_end, interval.start))
            prev_end = interval.end

    return result


def main():

    # result = [3, 5]
    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    # result = [4,6], [8,9]
    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    # result = [5,7]
    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
