https://practice.geeksforgeeks.org/problems/min-number-of-flips/0

#include <bits/stdc++.h> 
using namespace std;

int flip(string str, char expected) 
{ 
    int flipCount = 0; 
    for (int i = 0; i < str.length(); i++) 
    { 
        if (str[i] != expected) 
            flipCount++; 
        expected = (expected == '0') ? '1' : '0'; 
    } 
    return flipCount; 
} 
  

int main() {
    int t;
    //string s;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        cout<<min(flip(s,'0') , flip(s,'1'))<<"\n";
        
    }
    
	//code
	return 0;
}
