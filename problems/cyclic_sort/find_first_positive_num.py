"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Time complexity: O(n)
Space complexity: O(1)
"""

def solution(A):
    i = 0

    # cyclic sort all numbers A[i] in which 0 < A[i] <= len(A)
    # to their corresponding index
    while i < len(A):
        j = A[i] - 1 # index the item should be at
        if A[i] > 0 and A[i] <= len(A) and A[i] != A[j]:
            A[i], A[j] = A[j], A[i]  # swap
        else:
            i += 1
    
    # find the first number that is not at its correct index
    for idx, num in enumerate(A):
        if num != idx + 1:
            return idx + 1
    
    return len(A) + 1
