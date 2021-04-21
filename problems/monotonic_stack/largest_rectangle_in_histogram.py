"""
Given an array of integers heights representing the histogram's bar height where 
the width of each bar is 1, return the area of the largest rectangle in the histogram.

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # i is the index of the bar whose height is the height of a candidate rectangle
        # l is the first index of a bar to the left with height h[l] < h[i]
        # r is the first index of a bar to the right with height h[r] < h[i]
        
        max_area = 0
        indexes = [-1]
        heights.append(0) # ensures "indexes" stack will never be empty
        # also ensures that all heights > 0 will be popped from stack when you reach
        # the end of the heights array
        
        for r, height in enumerate(heights):
            while heights[indexes[-1]] > height:
                i = indexes.pop()
                h = heights[i]
                w = r - indexes[-1] - 1 # right - left - 1
                max_area = max(max_area, h*w)
            indexes.append(r)
        
        heights.pop()
        return max_area