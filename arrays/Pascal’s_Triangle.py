#Question Name
#Pascal's Triangle
#pattern 
# Primary = Dynamic Programming (must)
# Secondary = Simulation (optional)

#Approch

#Build each row from the previous one by padding it with zeros on both sides
#  and summing adjacent elements. This avoids boundary checks and 
# naturally forms Pascal’s Triangle.

#Leetcode Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]

        for i in range(numRows-1):
            temp=[0]+res[-1]+[0]
            r=[]
            for j in range(len(res[-1])+1):
                r .append(temp[j]+temp[j+1])
            res.append(r)
        
        return res
#testcase
# 5
# 1

#optimal approch alternative 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            row = [1] * (i + 1)  

            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]

            res.append(row)

        return res