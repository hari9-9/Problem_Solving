#include <bits/stdc++.h>

using namespace std;

// Complete the alternatingCharacters function below.
int alternatingCharacters(string s) {
    int l;
    l=s.length();
    char lis[l];
    int sum=0,i;
    lis[0]=s[0];
    int k=1;
    for(i=1;i<l;i++)
    {
        if(s[i]!=lis[k-1])
        {
            lis[k]=s[i];
            k++;
        }
        else
        {
            sum++;
        }
    }
    return sum;


}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s;
        getline(cin, s);

        int result = alternatingCharacters(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
