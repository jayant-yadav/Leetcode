from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                if i!=j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
        for i in range(n):
            for j in range(int(n/2)):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]


        return matrix
        

if __name__ == '__main__':
    sol = Solution()
    matrix = sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

    n = len(matrix)

    for i in range(n):
        for j in range(n):
            print(matrix[i][j]," ", end="")
        print('\n')