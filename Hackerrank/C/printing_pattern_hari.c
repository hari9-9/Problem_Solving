#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
    int i ,j ,k;
    for(i=1;i<2*n;i++)
    {
        k=n;
        if(i<=n)
        {
            for (j=1;j<2*n; j++)
            {
                printf("%d " , k);
                if(i>j)
                {
                    k-=1;
                }
                if(i+j >=2*n)
                {
                    k+=1;
                }
            }
        }
        if(i>n) 
        {
            for (j=1;j<2*n ; j++)
            {
                printf("%d " , k);
                if(j>=i)
                {
                    k+=1;
                }
                if(i+j <2*n)
                {
                    k-=1;
                }
            }
        }
    printf("\n");    
    }
  	// Complete the code to print the pattern.
    return 0;
}
