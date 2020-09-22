class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int n=A.size();
        int m=A[0].size();
        int s,e,temp;
        int i,j;
        for(i=0;i<n;i++)
        {
            for(s=0,e=m-1;s<m/2;s++,e--)
            {
                temp=A[i][s];
                A[i][s]=A[i][e];
                A[i][e]=temp;
            }
            for(s=0;s<m;s++)
            {
                A[i][s]= A[i][s]==0 ? 1:0;
            }
        }
        return A;
        
    }
};
