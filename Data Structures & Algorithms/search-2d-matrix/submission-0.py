class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        if not matrix:
            return False # if emtpy

        '''
        The entire matrix is sorted

        cur < target  ; cur and everything to the left isnt target
        cur > target ; cur and everyhting to the right isnt target
        
        cur == target then true

        mid_row = row count // 2
        m = len(matrix) leng of col
        n = len(maxtrix[0]) leng of rows
        m x n = total elements
        
        12 total
        i = 0
        j = m X n - 1 // its 1 indexed to we make it 0 idnexed

        mid =  j - i / 2 
        mid = 11 - 0
        mid = 11 / 2
        mid = 5

        5 / n = 
        5 / 4 = 1 r 1 // we use this to recalculate the 2d form


        '''


        m = len(matrix) #leng of col
        n = len(matrix[0]) #leng of rows

        i = 0
        j = m * n - 1 # its 1 indexed to we make it 0 idnexed

        while i <= j:
            
            mid =  j - i // 2

            cur_r = int(mid // n)
            cur_c = int(mid % n)


            if matrix[cur_r][cur_c] < target:
                i = mid + 1

            elif matrix[cur_r][cur_c] > target:
                j = mid - 1
            else:
                return True





        return False
