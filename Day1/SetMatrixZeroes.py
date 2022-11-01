"""
Time complexity:O(MxN)
Space complexity:O(1)
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
   
        R = len(matrix)
        C = len(matrix[0])
      
        # Mark first column and remaining first row and column elements
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
               
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # Set remaining row and column elements
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
                    
        # Set first row elements
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
                
        # Set first column elements
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
