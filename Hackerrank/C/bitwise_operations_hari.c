#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

#define MAX(a,b) (((a)>(b))?(a):(b))
void calculate_the_maximum(int n, int k) {
    int max_and= 0;
    int max_or = 0;
    int max_xor= 0;
    int cal;
    int i,j;
    for(i=1;i<=n;i++)
    {
        for(j=i+1 ; j<=n;j++)
        {
            cal =MAX(i&j, max_and);
            if(cal < k)
            {
               max_and = cal; 
            }
            cal =MAX(i|j, max_or);
            if(cal < k)
            {
               max_or = cal; 
            }
            cal =MAX(i^j, max_xor);
            if(cal < k)
            {
               max_xor = cal; 
            }
        }
    }
    printf("%d\n%d\n%d\n" , max_and , max_or , max_xor);
  //Write your code here.
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}

