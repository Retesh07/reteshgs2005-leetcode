bool increasingTriplet(int* nums, int numsSize) {
    int l = numsSize;
    int first = INT_MAX;
    int second = INT_MAX;
    for(int i =0;i<l;i++){
        if(nums[i]<=first){
            first = nums[i];
        }
        else if (nums[i]<=second){
            second = nums[i];

        }
        else{
            return true;
        }

    }
    return false;

    
}