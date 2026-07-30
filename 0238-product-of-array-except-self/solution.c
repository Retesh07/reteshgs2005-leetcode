int* productExceptSelf(int* nums, int numsSize, int* returnSize) {

  

    *returnSize = numsSize;

   
    int* n = (int*)malloc(numsSize * sizeof(int));
   

    n[0] = 1;
    for (int i = 1; i < numsSize; i++) {
        n[i] = n[i - 1] * nums[i - 1];
    }

 
    int m = 1;
    for (int i = numsSize - 1; i >= 0; i--) {
        n[i] = n[i] * m;   
        m = m * nums[i];
    }

    return n;
}