# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        goal: find if a linked list has a cycle

        brute force: 
        track ever nodes address, if we repeat address then we have a cycle
        if we dont loop ends and we exit knowing no cycle

        we use a hash set tracking all uniuqe nodes pointers/addresses
        so o(n) space worst 
        
        Issue we have to add every nodes address into the set

        Optimized:
        To get O(1) space we essentaily wouldnt store anything knew to what we are given
        I'm thinking what if we use two pointers
        Treat it almost like a track we have one pointer move twice as fast as the first pointer
        if the fast pointer ever laps the first one then we know that there is a cycle
        if the fast pointer finishes / dosn't pass the slow one we know there isnt a cycle
        '''
        if not head:
            return False

        # n_set = set()
        fast = head.next # to avoid errors at start line with checkign if same node
                        # Also auto ends if only 1 node linked list
        slow = head
        
        while fast != None:
            # if cur in n_set:
            #     return True

            # n_set.add(cur)

            if fast == slow:
                return True

            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            

        
        return False