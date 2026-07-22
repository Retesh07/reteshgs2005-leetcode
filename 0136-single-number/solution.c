int singleNumber(int* nums, int numsSize) {
    int l = numsSize;
    int result = 0;
    for(int i=0;i<l;i++){
        result ^= nums[i];
    }
    return result;

    
}