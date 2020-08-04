#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
// %d (integer), %c (character), %s (string), %f (float)
// To input two integers separated by a space on a single line, the command is scanf("%d %d", &n, &m),
int main()
{
    int a,b;
    float c,d;
    scanf("%d %d" , &a , &b);
    scanf("%f %f" , &c , &d);
    printf("%d %d\n", a+b , a-b);
    printf("%0.1f %0.1f\n" ,c+d , c-d);
	
    
    return 0;
}
