#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch;
    scanf("%c", &ch);
    char s[100];
    scanf("%s",&s);
    char sen[100];
    //scanf("\n"); notice the space before % to avoid new line apparently
    scanf(" %[^\n]%*c", &sen);
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);


    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
