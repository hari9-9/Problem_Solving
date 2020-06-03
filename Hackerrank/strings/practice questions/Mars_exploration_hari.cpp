#include <bits/stdc++.h>

using namespace std;

// Complete the marsExploration function below.
int marsExploration(string s) {
    string ref="SOS";
    int count=0;
    int i,l;
    l=s.length();
    for(i=0;i<l;i++)
    {
        if(ref[i%3]!=s[i])
        {
            count++;
        }
    }
    return(count);


}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = marsExploration(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
