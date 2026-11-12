class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # see if target exists in nums arr
        # we need some sort of loop 

         
        l = 0
        r = len(nums) - 1# maybne -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:

                r = mid - 1
                
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

            

        return -1


        '''
        Main goal is to find if target exists as fast as possible
        Array is sorted, 
        We can compare the vlaue of target to the value were at 


        '''
        