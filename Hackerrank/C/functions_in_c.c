#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a, int b ,int c, int d)
{
    int m=a;
    if(b>m)
    {
        m=b;
    }
    if(c>m)
    {
        m=c;
    }
    if(d>m)
    {
        m=d;
    }
    return m;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
