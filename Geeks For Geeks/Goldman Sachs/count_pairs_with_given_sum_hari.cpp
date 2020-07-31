 // https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum/0

#include <stdio.h>
#include <bits/stdc++.h> 
using namespace std;
int getpair(int n ,int sum ,int arr[])
{
    unordered_map<int, int> m; 
    for (int i=0; i<n; i++) 
        m[arr[i]]++; 
  
    int twice_count = 0; 
    for (int i=0; i<n; i++) 
    { 
        twice_count += m[sum-arr[i]];
        if (sum-arr[i] == arr[i]) 
            twice_count--;
    } 
    return twice_count/2; 
} 

int main() {
    int t,n,k,i;
    cin>>t;
    while(t--)
    {
       cin>>n;
       cin>>k;
       int arr[n];
       for(i=0;i<n;i++)
       {
           cin>>arr[i];
       }
       cout<<getpair(n,k,arr)<<"\n";
        
    }
	//code
	return 0;
}
