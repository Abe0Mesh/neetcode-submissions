class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        goal: find smallest value in the array

        rotaiting # = len of list > original list

        brute:
        - sort the array
        - run a min search

        optimiation:
        - use the accending order to navigate/jump around to find smallest val
        - To the left of the smallest val is a bigger number
        - Binary search using logic above
        - EDGE: need to ahndle cases where max/min are at ends
        - Dont check == as all vals are unique

        '''

        # [3,4,5,6,1,2] i < j # 3 > 2
        # i = 0, j = 5
        # mid = 2

        # i < mid
        # 3 < 5 -> i is now mid + 1
        # [6,1,2]
        # 6 < 1 if mid-1 


        # while i <= j

        # iv < ij
        # i-1




        # start with 4
        # we check is the value to the left bigger or smaller then i
        # val < left means min ... 
        # else val > left, 





        return min(nums)
