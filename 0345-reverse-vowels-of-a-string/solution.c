char* reverseVowels(char* s) {
    int l = strlen(s);
    int i=0;
     char* c = (char*)malloc(l * sizeof(char)); 
     int vowel = 0;
    while(i<l){
        if (s[i] == 'a' || s[i] == 'A' || s[i] == 'e' || s[i] == 'E' ||
    s[i] == 'i' || s[i] == 'I' || s[i] == 'o' || s[i] == 'O' ||
    s[i] == 'u' || s[i] == 'U') {
        c[vowel++]=s[i];



        }
        i++;
    }
    vowel--;
    for(int i=0;i<l;i++){
         if (s[i] == 'a' || s[i] == 'A' || s[i] == 'e' || s[i] == 'E' ||
    s[i] == 'i' || s[i] == 'I' || s[i] == 'o' || s[i] == 'O' ||
    s[i] == 'u' || s[i] == 'U') {
        s[i]=c[vowel--];



        }

    }
    return s;
    
}