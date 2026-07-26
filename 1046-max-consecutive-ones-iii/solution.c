int longestOnes(int* nums, int numsSize, int k) {
    int l=0;
    int r=0;
    int zero_count=0;
    int max =0;
    
    while(r<numsSize){
        if(nums[r]==0){
            zero_count++;
        }
        if(zero_count>k){
            if(nums[l]==0){
                zero_count--;
            }
            l++;
        }
        if(zero_count <= k){
            int len = r-l+1;
            if(len>max){
                max = len;
            }

        }
        r++;

    }

    return max;
    
}