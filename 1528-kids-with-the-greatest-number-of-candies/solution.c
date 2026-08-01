/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    *returnSize = candiesSize;
    bool *r = (bool*)malloc(candiesSize * sizeof(bool));
    int l = candiesSize;
    int extra = extraCandies;
    int g = candies[0];
    for(int i=1;i<l;i++){
           if(candies[i]>=g){
            g = candies[i];
           }      
    }
    for(int j=0;j<l;j++){
        if((candies[j]+extra)>=g){
            r[j]=1;
        }
        else{
            r[j]=0;
        }

    }
    return r;

    
}