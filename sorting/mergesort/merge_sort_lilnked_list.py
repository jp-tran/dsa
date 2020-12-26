# Top-down implementation of merge sort for a singly-linked list
# O(n log(n)) time, where n is the number of nodes
# O(log(n)) space for the recursive call stack

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        mid = self.getMid(head) # find the middle node
        left = self.sortList(head) # sort list on left side
        right = self.sortList(mid) # sort list on right side
        return self.mergeSortedLists(left, right)
        
    def getMid(self, node):
        # assume input list has at least 2 nodes
        # "fast" pointer advances twice as fast as "slow" pointer
        slow = None
        fast = node
        while fast and fast.next:
            slow = node if slow is None else slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None # break the pointer pointing to the middle node
        return mid
    
    def mergeSortedLists(self, node1, node2):
        head = ListNode()
        node = head
        
        # iteratively redirect pointers to create one sorted list
        # until one list is completely traversed
        while node1 and node2:
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next
            elif node1.val > node2.val:
                node.next = node2
                node2 = node2.next
            node = node.next
        
        # point to the nodes of the remaining list
        if node1:
            node.next = node1
        elif node2:
            node.next = node2
        return head.next