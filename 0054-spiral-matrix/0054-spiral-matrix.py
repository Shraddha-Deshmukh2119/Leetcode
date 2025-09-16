from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        total = r * c
        ans = []
        count = 0   # ✅ renamed `c` to `count` so it won’t clash with columns

        rowstart = 0
        rowend = r - 1   # ✅ should be last row index
        colstart = 0
        colend = c - 1   # ✅ should be last column index

        while count < total:
            # Traverse left → right
            for i in range(colstart, colend + 1):
                if count < total:
                    ans.append(matrix[rowstart][i])
                    count += 1
            rowstart += 1

            # Traverse top → bottom
            for i in range(rowstart, rowend + 1):
                if count < total:
                    ans.append(matrix[i][colend])
                    count += 1
            colend -= 1

            # Traverse right → left
            for i in range(colend, colstart - 1, -1):
                if count < total:
                    ans.append(matrix[rowend][i])
                    count += 1
            rowend -= 1

            # Traverse bottom → top
            for i in range(rowend, rowstart - 1, -1):
                if count < total:
                    ans.append(matrix[i][colstart])
                    count += 1
            colstart += 1

        return ans
