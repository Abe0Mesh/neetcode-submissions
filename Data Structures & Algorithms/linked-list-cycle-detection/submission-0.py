# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        '''
        Goal: Determine if a cycle exists in the linked list

        brute force:
        we search through each node of the linked list, along with a set that tracks each value we see
        if we happen to add a duplicate value to the set we know a cycle exists, and we can exit true

        if we finish looking throiugh entire linked list then we retrun false 

        node_set = set()
        cur = head

        while cur != none
        # here we will add values to set, check if they exist and then react/iterate

        ... WAIT I just reailzied they dont garentee that values will be unique, so waht if its like 1-> 1 -> 1
        that would say yeah thats a cycle when its not

        optimization:
        - I thinking what if I track the address/refeences of all visited nodes and then check each time if that visited node address exisits in the set
        '''


        node_set = set()
        cur = head

        while cur != None:
            if cur in node_set:
                return True
            
            node_set.add(cur)

            cur = cur.next
        
        return False
        