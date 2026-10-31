class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Do not sort heights as orignal order matters

        max_vol = 0

        # what if we had the outer loop be i < j, and we move i and j based on which has the shorter height
        i = 0
        j = len(heights) - 1

        # We can also predict the max value of a future height by being like okay so left pointers height is like
        # 3, so we know if we move the pointer only can be width * 3 so fi we have something bigger then that
        # we could stop looping early
        while i < j:

            width = j  -  i
            
            min_height = min([heights[i], heights[j]])
            if width * min_height > max_vol:
                    max_vol = width * min_height

            if heights[i] > heights[j]:    
                j -= 1

            else:
                i += 1





        #         height = min([heights[i], heights[j]])


        # for i in range(len(heights)):
        #     height = heights[i] 

        #     # So each check we gonna have to calculate area using the smaller height
        #     j = len(heights) - 1

        #     while i < j:
        #         # only dec j 

        #         width = j  -  i
        #         height = min([heights[i], heights[j]])
                
        #         if width * height > max_vol:
        #             max_vol = width * height
        #         j -= 1





        return max_vol