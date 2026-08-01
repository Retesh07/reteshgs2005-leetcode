int minSubArrayLen(int target, int* nums, int numsSize) {
    int left=0;
 
    int sum=0;
    int min = INT_MAX;
    int l = numsSize;
    for(int right =0;right<l;right++){
        if(nums[right]==target || nums[right]>target){
            return 1;
        }
        sum = sum + nums[right];
        while(sum>=target){
            int k = right - left + 1;
            if(k<min){
                min=k;
            }
            sum = sum - nums[left];
            left++;
            

        }
    }
    return (min==INT_MAX)?0:min;
    
}