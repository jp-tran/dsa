"""
Design a rate limiter that limits the number of times clients can hit an API within
a given time window.

Time complexity: amortized O(1)
Each item is only added to and removed from the queue once.

Space complexity: O(n)
where n is the number of valid hits within any given time window
"""

from collections import deque, defaultdict

class RateLimiter:
    def __init__(self, max_hits, window_seconds):
        self.queue = deque() # queue item is a tuple (client id, hit time)
        self.clients = defaultdict(int)
        self.max_hits = max_hits
        self.window = window_seconds
        
    def hit(self, client_id, current_time):
        """ If the client `client_id` has called hit() fewer than max_hit 
        times in the last window_seconds, record the hit and return True
        else return False
        """
        # pop from left end of queue
        while self.queue and self.queue[0][1] < current_time - self.window:
            earliest = self.queue.popleft()
            if self.clients[earliest[0]] == 1:
                del self.clients[earliest[0]]
            else:
              self.clients[earliest[0]] -= 1
             
        
        # append new hit to queue if it's a valid hit
        if self.clients[client_id] < self.max_hits:
            queue.append((client_id, current_time))
            self.clients[client_id] += 1
            return True
        
        return False