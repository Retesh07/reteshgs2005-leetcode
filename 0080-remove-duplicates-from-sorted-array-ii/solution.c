int removeDuplicates(int* nums, int numsSize) {
  int i=1;
  for(int j=1;j<numsSize;j++){
    if(i<2 || nums[i-2]!=nums[j]){
        nums[i]=nums[j];
        i++;
    }
  }
return i;
    
}