class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort() 
        fin = []

        for i in range(len(nums) - 2):
            if i > 0:
                if nums[i - 1] == nums[i]:
                    continue

            # nums=[-1,0,1,2,-1,-4]
            j = i + 1
            k = len(nums) - 1
            while j < k:


                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    fin.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1

                    
                
                elif total > 0:
                    k -= 1

                else: # total < 0
                    j += 1
        
        return fin