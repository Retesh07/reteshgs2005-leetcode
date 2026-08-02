void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
   
 int i=0,j=0,k=0;
 int temp[m+n];
 while(i<m && j<n){
    if(nums1[i]<=nums2[j]){
        temp[k++]=nums1[i];
        i++;

    }
    else{
        temp[k++]=nums2[j];
        j++;
    }
    
 }
 while(i<m){
    temp[k++]=nums1[i++];
 }
 while(j<n){
    temp[k++]=nums2[j++];
 }
 for(int i=0;i<m+n;i++){
    nums1[i]=temp[i];
 }
    
}