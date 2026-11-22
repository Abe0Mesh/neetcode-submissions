class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        '''
        Goal : Find min element in O(log n) time

        Brute force:
        search every element and track smallest
        return min(nums), but O(N)

        Optimization:
        use a log n search

        Using bin search
        - we can use the fact taht this arr was sorted to know how to jump around 
        - arr is bascaily two sorted sections, 
        -- we know if we are in a sorted section (mid) if left <= mid, 
        -- if above isnt true it means evertything mid + 1 and r is sorted, as if we were to walk through every element from mid to l (by rotaitng / looping around) its garneteed to be sorted e.g [4,5,0,1,2,3] walking from 0 to 4 is garneted sorted 0 to 3

        we can use this logic to enter on of these sorted sections and perform a log search inside of it as we instantly know where the min val is

        '''

        l = 0
        r = len(nums) - 1
        min_v = nums[0] # setting a default min value to a possible val inside of nums

        # nums=[4,5,6,7,0,1,2]
        # mid nums[3] = 7, l < mid true so l is now at 4 and min is 4

        # nums=[0, 1 ,2]
        # mid = nums[5] = 1
        # nums l < r true so we return l

        while l <= r:
            mid = (l + r) // 2

            if nums[l] <= nums[r]:
                # we know entire list is sorted and l is min value in the window so no need to continue checking
                min_v = min(min_v, nums[l])
                break

            # if above inst true then we still ahve two sorted sub arrs

            if nums[l] <= nums[mid]: # we are in a sorted section
                min_v = min(min_v, nums[mid]) 
                # move l pointer as we found the smallest val from l to mid
                l = mid + 1

            else: # if nums[l] > nums[mid]
                # this means mid is in a dif sub arr, mid to r, so mid would be smallest value from mid to r
                min_v = min(min_v, nums[mid])
                r = mid - 1




        return min_v



