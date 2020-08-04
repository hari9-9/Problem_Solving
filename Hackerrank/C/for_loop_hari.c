#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    char outputs[11][6] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "even", "odd"};
    scanf("%d\n%d", &a, &b);
    int i,ele;
    for(i=a;i<=b;i++)
    {
        if(i<=9)
        {
            ele = i-1;
        }
        else if(i%2 == 0)
        {
            ele = 9;
        }
        else
        {
            ele = 10;
        }
        printf("%s\n" , outputs[ele]);
    }
  	// Complete the code.

    return 0;
}
