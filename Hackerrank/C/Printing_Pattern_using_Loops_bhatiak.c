#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);

    int m = (2*n)-1;
  	
    int arr[m][m];

    for(int k=0; k<n; k++) {
        for(int i=k; i<n; i++) {
            for(int j=k; j<n; j++) {
                arr[i][j]= n-k;
                arr[m-i-1][j] = n-k;
                arr[i][m-j-1] = n-k;
                arr[m-i-1][m-j-1] = n-k;
            }
        }
    }

    for (int i=0; i<m; i++) {
        for (int j=0; j<m; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
