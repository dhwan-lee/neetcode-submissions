class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = 0
        
        for row in matrix:
            if target >= row[0]:
                index += 1
            else:
                break
        
        for value in matrix[index - 1]:
            if target == value:
                return True

        
        return False
            