class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #use binary search for every row
        #if the right index reaches the column length-1 then increment the row
        l, r = 0, len(matrix[0]) - 1
        end = len(matrix)-1
        for row in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                mid = (l+r)//2 
                if matrix[row][mid] < target:
                    l = mid +1 
                elif matrix[row][mid] > target:
                    r = mid - 1
                else:
                    return True

        return False
