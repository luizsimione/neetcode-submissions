class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0]) # number of columns

        low, high = 0 , rows * cols - 1

        binarySearch = rows * cols

        while low <= high:
            mid = low + (high - low) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

        