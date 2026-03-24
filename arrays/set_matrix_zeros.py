#Question: Set Matrix Zeros
#pattern: Matrix Marking 

# Approch 
# Store rows and columns containing 0
# update matrix in 2nd pass

#leetcode Solution 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        width,height=len(matrix),len(matrix[0])
        col_to_change=[]
        row_to_change=[]

        for row in range(width):
            for col in range(height):

                if matrix[row][col]==0:

                    col_to_change.append(col)
                    row_to_change.append(row)

        col_to_change=set(col_to_change)
        row_to_change=set(row_to_change)


        for c in col_to_change:
            for row in range(width):
                matrix[row][c]=0

        for r in row_to_change:
            for col in range(height):
                matrix[r][col]=0

        return matrix
    
    # test cases 
    # [[1,0,1],[0,0,0],[1,0,1]]
    # [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
