# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        '''
        goal: Reverse the list 

        brute force: 
        while next != none
        we go through the list and we swap the .next value to the node to the left
        - we skip head for this one 
        
        e.g 
        [0,1,2,3]
        - skip 0
        - set 1's next to 0
        set 2's next to 1

        now im trying ot figure out ho wot handle this as the loop would stop at next != none
        so we could do this after loop runs, 
        set 3's next to 2 and set to head



        new e.g
        [0,1,2,3]
        cur: val = 0, next = 1

        temp_next = 1 (address)
        cur.next = none
        before = cur (0)
        cur = temp_next



        
        and what if I used a two pointer setup, so I have a pointer for like to the left and one with cur
        im like cur.next = before(pointer)
        

        '''
        cur = head
        before = None

        while cur != None:
            # curs head is two
            # cur is 1
            # we want cur's next to be head
            temp_next = cur.next
            cur.next = before
            before = cur
            cur = temp_next 

        return before

        




        