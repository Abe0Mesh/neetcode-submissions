# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        Goal: return a new merged linked list

        brute force:

        loop through both and add values all values into a array
        sort array 
        create a new linked list 

        optimized:
        Use the already exists nodes from the linked list and just move their pointers around

        we can start with using a dummy node to give us a starting point so we dont need to find a 
        starting head

        we can use a while loop, running until one or both of the link lists walk through pointers point at none
        meaning we've checked all nodes in said list

        dummy = ListNode() # temp head
        cur = dummy

        while list1 not None and list2 not None:
            if list1.val <= list2.val:
                # we add list 1s val to new list  then iterate
                cur.next = list1
                list1 = list1.next 

            else: # list 1 > list 2 
                # we then add list two and iterate
                cur.next = list2
                list2 = list2.next 

        Then after this loop we have two possible cases, list 1 has left overs or list 2 has left overs

        either case we set cur.next = list1/2, we basicaly just tether on the reast of the unsearch nodes to the end of our new node

        at the end we then just return dummy.next, as dummy was just a place holder the actualy head is the
        next value 

        test case [1,2] [1,3]

        cur = dummy, 

        1. [dummy, 1]
        2. dummy, 1, 1
        3. 
        '''


        dummy = ListNode() # temp head
        cur = dummy
        # cur = dummy
        # cur.next = none
        # loop 1 
        # [dummy, 1]
        # list1 = list1.next , so here we change the 

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                # we add list 1s val to new list  then iterate
                cur.next = list1
                cur = cur.next
                list1 = list1.next 

            else: # list 1 > list 2 
                # we then add list two and iterate
                cur.next = list2
                cur = cur.next
                list2 = list2.next 

        if list1 != None :
            cur.next = list1
        
        if list2 != None:
            cur.next = list2

        return dummy.next



