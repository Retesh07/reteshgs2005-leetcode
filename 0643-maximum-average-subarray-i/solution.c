double findMaxAverage(int* nums, int numsSize, int k) {
    int sum=0;
    for(int i=0;i<k;i++){
        sum+=nums[i];
    }
    int max = sum;
    for(int j=k;j<numsSize;j++){
        sum+=nums[j]-nums[j-k];
        if(sum>max){
            max = sum;
        }
    }
   
   return (double)max / k;
}