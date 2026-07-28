bool isSubsequence(char* s, char* t) {
    
    int l1=strlen(s);
    int l2=strlen(t);
    int j=0;
    if(l1== NULL && l2== NULL){
        return true;
    }
    for(int i=0;i<l2;i++){
        if(s[j]==t[i]){
            j++;
        }
        if(j==l1){
            return true;
        }
      
       
       
    }
    return false;
    
}