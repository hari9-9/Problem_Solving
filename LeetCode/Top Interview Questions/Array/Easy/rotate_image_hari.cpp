class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n= matrix.size();
        cout<<n;
        int i,j,temp;
        // transpose
        for (i=0;i<n;i++)
        {
            for(j=i;j<n;j++)
            {
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        //swap columns
        for (i=0;i<n;i++)
        {
            for(j=0;j<(n/2);j++)
            {
                temp = matrix[i][j];
                matrix[i][j] =matrix[i][n-1-j];
                matrix[i][n-1-j] = temp;
                
                
            }
        }
    }
};


// second attempt

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int i,j;
        int temp;
        int n=matrix.size();
        for(i=0;i<n;i++)
        {
            for(j=i;j<n;j++)
            {
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n/2;j++)
            {
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][n-j-1];
                matrix[i][n-j-1] = temp;
            }
        }
        
    }
};
