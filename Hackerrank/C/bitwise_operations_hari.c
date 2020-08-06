#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

#define MAX(a,b) (((a)>(b))?(a):(b))
void calculate_the_maximum(int n, int k) {
    int max_and= -1;
    int max_or = -1;
    int max_xor= -1;
    int cal;
    int i,j;
    for(i=1;i<=n-1;i++)
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
    printf("%d\n%d\n%d" , max_and , max_or , max_xor);
  //Write your code here.
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
