// https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x/0

unable to submit but logic verified

#include <iostream>
using namespace std;
int main() {
    int t,n,x,i,min_avail,curr_sum,start,end;
    cin>>t;
    while(t--)
    {
       cin>>n;
       cin>>x;
       int arr[n];
       for(i=0;i<n;i++)
       {
           cin>>arr[n];
       }
       min_avail=n+1;
       start=0;
       end =0;
       curr_sum = 0;
       while(end<n)
       {
           while(curr_sum <= x && end<n)
           {
               curr_sum+=arr[end++];
           }
           while(curr_sum >x && start<n)
           {
                if (end - start < min_avail) 
                    min_avail = end - start; 
  
            // remove starting elements 
            curr_sum -= arr[start++];
           }
       }
       cout<<min_avail<<"\n";
    }
    
	//code
	return 0;
}
