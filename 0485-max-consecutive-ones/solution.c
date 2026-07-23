int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int i=0;
    int j=0;
    int max=0;
    while(j<numsSize){
        if(nums[j]==1){
           i++;

        }
        else{
            i=0;
        }
        if(i>max){
            max = i;
        }
        j++;



    }
    return max;
    
}