bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    int l = flowerbedSize;
    int count = 0 ;
   
    for(int i =0;i<l;i++){
        if(flowerbed[i]==0){

        int prev = (i==0)? 0:flowerbed[i-1];
        int next = (i == l-1) ? 0 : flowerbed[i+1];
        if(prev==0 && next==0){
            count++;
            flowerbed[i]=1;
        }
     }

    }
    return (count>=n);
    
}