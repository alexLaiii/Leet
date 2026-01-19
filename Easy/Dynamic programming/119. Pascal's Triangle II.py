class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prevRow = [1,1]

        for i in range(rowIndex - 1):
            currRow = [1]
            for j in range(1, len(prevRow)):
                currRow.append(prevRow[j] + prevRow[j - 1])
            
            currRow.append(1)
            prevRow = currRow

        return prevRow
                
