class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int i;
        int n= T.size();
         vector<int>temp(n,0);
        for(i=0;i<n;i++)
        {
            int j=i+1;
            while(j<n)
            {
                if(T[j]>T[i])
                {
                   temp[i]=j-i;
                    break;
                }
                j++;
            }
        }
        return temp;
        
    }
};
