 // https://practice.geeksforgeeks.org/problems/ugly-numbers/0
 

#include <bits/stdc++.h> 
using namespace std;
bool isUgly(int num) {
    if(num==0)
        return false;
    while(num%2==0)
        num/=2;
    while(num%3==0)
        num/=3;
    while(num%5==0)
        num/=5;
    return num==1? true : false;
        
    }
int main() {
    int t,n,i,count;
    cin>>t;
    while(t--)
    {
        cin>>n;
        i=1;
        count =1;
        while(count<n)
        {
            i++;
            if(isUgly(i))
            {
                count++;
            }
            
        }
        cout<<i<<"\n";
        
    }
	//code
	return 0;
}
