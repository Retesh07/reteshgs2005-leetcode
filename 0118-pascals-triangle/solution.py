class Solution(object):
    def generate(self, numRows):
        output = []
        for i in range(numRows):
            temp = []
            mul = 1
            for j in range(i + 1):
                temp.append(mul)
                mul = mul * (i - j) // (j + 1)
            output.append(temp)
        return output
