#include <bits/stdc++.h>

using namespace std;
 int CHARS=26;
// Complete the makeAnagram function below.
int makeAnagram(string a, string b) {
    int c1[CHARS]={0};
    int c2[CHARS]={0};
    int s=0;
    int i;
    for(i=0;a[i]!='\0';i++)
    {
        c1[a[i]-'a']++;
    }
    for(i=0;b[i]!='\0';i++)
    {
        c2[b[i]-'a']++;
    }
    for(i=0;i<26;i++)
    {
        s+=abs(c1[i]-c2[i]);
    }

    return(s);

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a;
    getline(cin, a);

    string b;
    getline(cin, b);

    int res = makeAnagram(a, b);

    fout << res << "\n";

    fout.close();

    return 0;
}
