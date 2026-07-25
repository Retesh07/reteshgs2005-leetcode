bool isPalindrome(char* s) {
    
     int n = strlen(s);
    char* t = (char*)malloc(n+1);
   
    int j=0;
    for(int i=0;i<n;i++){
        if(isalnum(s[i])){
            t[j++]= tolower(s[i]);
        }
    }
    t[j]='\0';
    if(s==""){
        return true;
    }
    int l = strlen(t);
     
    for(int k=0;k<l/2;k++){
        if(t[k]!=t[l-k-1]){
            return false;
        }

    }
    return true;
    
}