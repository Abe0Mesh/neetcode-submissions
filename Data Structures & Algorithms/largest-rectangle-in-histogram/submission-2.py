class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0

        # a col cant continue if the colum to the right is smaller then it, if its = > it can continue
        r = [] # start index w height

        #Input: heights = [7,1,7,2,2,4]
        # (0, 7) > 1

        for i in range(0, len(heights)):
            start = i
            while r and r[-1][1] > heights[i]:
                a = r.pop()
                new = ( (i - a[0]) * a[1])
                if new > max_area:
                    max_area = new
                start = a[0]

                    # Need to handle shortening the start index to the left 
                
            r.append((start, heights[i]))

        while r:
            a = r.pop()
            i = len(heights)
            new = ( (i - a[0]) * a[1]) 
            if new > max_area:
                max_area = new

        
        return max_area