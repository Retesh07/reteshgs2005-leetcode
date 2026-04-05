class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        d=defaultdict(list)

        for num in nums:
            if num==0:
                largest,smallest=0,0
            else:
                largest,smallest=0,float('inf')
                k=num
                while k:
                    m=k%10
                    if m>largest:
                        largest=m
                    if m<smallest:
                        smallest=m
                    k=k//10
            target = abs(largest-smallest)
            d[target].append(num)
        j=max(d.keys())
        sums=0
        for s in d[j]:
            sums+=s
        return sums
            
                
            
        
        