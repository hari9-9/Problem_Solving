#include <iostream>
#include <string.h>
using namespace std;

int main() {
	//code
	int t;
	string s;
	cin >> t;
	bool f;
	while(t--)
	{
	    f=false;
	    cin>>s;
	    for(int i=0 ; i<s.size() ; i++)
	    {
	        char e = s[i];
	        int k=i+1;
	        while(s[k])
	        {
	            if(s[i] == s[k])
	            {
	                cout<<s[i]<<'\n';
	                f=true;
	                break;
	            }
	            k++;
	        }
	        if(f==true)
	        {
	            break;
	        }
	    }
	    if(f==false)
	    {
	        cout<<-1<<"\n";
	    }

	}
	return -1;
}
