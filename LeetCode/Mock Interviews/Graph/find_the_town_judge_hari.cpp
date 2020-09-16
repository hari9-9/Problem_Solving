class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        bool graph[N+1][N+1];
        memset(graph,false,sizeof(graph));
        int i;
        for(i=0;i<trust.size();i++)
        {
            graph[trust[i][0]][trust[i][1]]=true;
        }
        for(i=1;i<=N;i++)
        {
            bool row=false;
            bool col=true;
            for(int j=1;j<=N;j++)
            {
                if(i!=j)
                    col &=  graph[j][i];
                row|= graph[i][j];
                //cout<<col<<" "<<row<<endl;
            }
            if(col && !row)
                return i;
        }
        return -1;
        
        
    }
};

// second implementation
class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        int t[N+1];
        memset(t,0,sizeof(t));
        for(int i=0;i<trust.size();i++)
        {
            t[trust[i][0]]--;
            t[trust[i][1]]++;
        }
        for(int i=1;i<=N;i++)
        {
            if(t[i]==N-1)
                return i;
        }
        return -1;
    }
};
