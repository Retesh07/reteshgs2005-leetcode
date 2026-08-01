int maxProfit(int* prices, int pricesSize) {
    int profit = 0;
    int buy=prices[0];
  
    int l = pricesSize;
    for(int i=1;i<l;i++){
        if(buy > prices[i]){
            buy = prices[i];
        }
        else if(buy < prices[i]){
            profit = profit + (prices[i]-buy);
            buy = prices[i];
        }



        
    }
    return profit;
    
}