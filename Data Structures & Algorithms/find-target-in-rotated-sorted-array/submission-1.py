class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
        goal: Find if target exisists in O(log n)

        brute force:
        Linear search through list O(n)

        optization:
        - bin search
        - check if we are cur in sorted arr with l <= mid
            - true: check if target is within this sub arr, l <= target <= mid 
            - if above true, move r to mid and do bin search
            - if false then move l to mid + 1

            - false: this means mid to r is sorted heck if target is within this sub arr, l <= target <= mid 
            - true: move l to mid and do bin search
            - false: mod r to mid - 1


        example
        [3,5,6,0,1,2]
        mid = 6, l = 3 , r = 2
        3 <= 4 <= 6 true so  r = 6, and do bin search
        [3,5,6]



        '''
        # nums=[5,1,3] 
        # mid is 1 

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]: # I realized its redudnet to check target insdie after
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else: 
                    l += 1
            else: # mid in right sub arr
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
                


        return -1

                
            # if nums[l] <= target <= nums[mid]: # I realized its redudnet to check target insdie after
            #     r = mid
            # else:
            #     l = mid + 1