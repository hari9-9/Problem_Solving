#include <bits/stdc++.h>

using namespace std;
static int T[5001][5001];

// Complete the commonChild function below.
int commonChild(string s1, string s2) {
    int m = s1.size();
    int n = s2.size();
    int i,j,k,kk;
    for(i = 0; i <= m; i++ ){
        for(j = 0; j <= n; j++ ){
            if(i == 0 || j == 0){
                T[i][j] = 0;
            }else if(s1[i-1]==s2[j-1]){
                T[i][j] = 1+T[i-1][j-1];
            }else{
                T[i][j] = max(T[i][j-1], T[i-1][j]);
            }
        }
        //cout<<i<<" "<<j<<"\n";
        //for(k=0;k<=m;k++)
        //{
        //    for(kk=0;kk<=n;kk++)
        //   {
        //        cout<<T[k][kk]<<" ";
        //    }
        //    cout<<"\n";
        //}
    }
    return(T[m][n]);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s1;
    getline(cin, s1);

    string s2;
    getline(cin, s2);

    int result = commonChild(s1, s2);

    fout << result << "\n";

    fout.close();

    return 0;
}
