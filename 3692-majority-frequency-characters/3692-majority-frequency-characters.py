class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        hashmp=defaultdict(int)
        for i in s:
            hashmp[i]+=1

        freq=defaultdict(list)
        v=0
        groupsize=0
        k=[]
        print(hashmp.items())
        
        for key,value in hashmp.items():
            freq[value].append(key)

            if groupsize<len(freq[value]):
                groupsize=len(freq[value])
                k=freq[value]
                v=value
            elif groupsize==len(freq[value]):
                if v<value:
                    k=freq[value]
                    v=value

                else:
                    k=freq[v]
            
              
        
                

        
        return ''.join(k)


        