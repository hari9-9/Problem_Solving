class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int count=0;
        int i;
        for(i=0;i<M.size();i++)
        {
            if(M[i][i]==1)
            {
                count++;
                dfs(M,i);
            }
        }
        return count;
        
    }
    
    void dfs(vector<vector<int>>& M,int v)
    {
        if(M[v][v]==0)
            return;
        for(int i=0;i<M.size();i++)
        {
            if(M[v][i]==1)
            {
                M[v][i]=0;
                dfs(M,i);
            }
        }
    }
};
