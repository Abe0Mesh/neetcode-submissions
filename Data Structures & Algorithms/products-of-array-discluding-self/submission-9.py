class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        


        postfix = []
        postfix.append(1)
        postInc = 0
        for i in range(len(nums)-2, -1, -1):
            postfix.append(nums[i+1] * postfix[postInc])
            postInc += 1 
            
            
        
        # for i in range(len(nums)-2, -1, -1): 
        #     postfix.insert(0, nums[i+1] * postfix[0]) 
   

        prefix = []
        prefix.append(1)  
        final = []
        final.append(postfix[len(postfix) - 1] * prefix[0])
        
        postInc = len(postfix) -2
        for i in range(1, len(nums)):
            prefix.append(nums[i-1] * prefix[i-1])

            final.append(postfix[postInc] * prefix[i])
            postInc -= 1
           


            #postfix = [ 48 ,24, 6, 1 ]
            # newpostfix = [1, 6, 24, 48]
            # prefix = [1, 1, 2, 8]


        return final

    # neet code talked about using pre fixes and post fixes to solve thius

    # calculate the prefix and post fix and add them together to find the value at each index
    
    # index 0 would have no prefix but 3 post fix being 2, 4, 6
    # index 1 pre : 1 post : 4 6
    # index 2 pre : 1 2 post 6
    # index 3 pre : 1 2 4 post : none


