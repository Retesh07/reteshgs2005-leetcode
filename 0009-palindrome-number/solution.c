bool isPalindrome(int x) {
    if(x<0){
        return false;
    }
    int m = x;
    long reverse = 0;
    int last =0;
    while(x>0){
        last = x % 10;
        x=x/10;
        reverse = (reverse*10) + (last);


    }
    return (reverse==m);
}