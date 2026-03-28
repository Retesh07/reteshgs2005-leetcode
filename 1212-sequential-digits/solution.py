class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
    
        output=[]

      
        for i in range(len(str(low)),len(str(high))+1):
            for j in range(1,11-i):
                m=""

                for k in range(j,j+i):
                    m+=str(k)
                if low<=int(m)<=high:
                    output.append(int(m))
        return output

            


        
        