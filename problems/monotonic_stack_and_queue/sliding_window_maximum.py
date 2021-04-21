"""
You are given an array of integers nums, there is a sliding window of 
size k which is moving from the very left of the array to the very right.
Find the maximum element in the window each time it slides.

Time complexity: O(n)
Space complexity: O(k) - not counting "ans" array
"""

from collections import deque

class MonotonicQueue:
    def __init__(self):
        self.queue = deque() # monotonic decreasing queue
    
    def push(self, n):
        while self.queue and self.queue[-1] < n:
            self.queue.pop()
        self.queue.append(n)
    
    def get_max(self):
        return self.queue[0]
    
    def popleft(self, n):
        if self.queue[0] == n:
            self.queue.popleft()

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = MonotonicQueue() # maintain monotonic decreasing queue
        
        for i, num in enumerate(nums):
            if i < k - 1:
                queue.push(num)
            else:
                queue.push(num)
                ans.append(queue.get_max())
                queue.popleft(nums[i-k+1])
        
        return ans
    