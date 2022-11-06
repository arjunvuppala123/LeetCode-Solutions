class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        res = [[1]]
        
        for i in range(1,numRows):
            curr = [1]
            for j in range(1,i):
                curr.append(res[i-1][j-1] + res[i-1][j])
            curr.append(1)
            res.append(curr)
        
        return res