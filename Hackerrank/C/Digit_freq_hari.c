#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int arr[] = {0,0,0,0,0,0,0,0,0,0,0};
    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    int i;
    for(i=0;i<strlen(s);i++)
    {
        arr[(int)(s[i])-48]++;
    }
    for(i=0;i<10;i++)
    {
        printf("%d ",arr[i]);
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
