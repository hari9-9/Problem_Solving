class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if(k==nums.size())
        {
            return nums;
        }
        unordered_map<int ,int>hmap;
        int i=0;
        int n=nums.size();
        for(i=0;i<n;i++)
        {
            hmap[nums[i]]++;
        }
        vector<int>val;
        vector<int>freq;
        for(auto& it:hmap)
        {
            val.push_back(it.first);
            freq.push_back(it.second);
            cout<<it.first<<" "<<it.second<<endl;
        }
        int temp;
        bool swap;
        vector<int>ans;
        int j;
        for(i=0;i<freq.size();i++)
        {
            swap=false;
            for(j=0;j<freq.size()-i-1;j++)
            {
                if(freq[j]<freq[j+1])
                {
                    swap=true;
                    temp=freq[j];
                    freq[j]=freq[j+1];
                    freq[j+1]=temp;
                    temp=val[j];
                    val[j]=val[j+1];
                    val[j+1]=temp;
                    
                                
                }
            }
            if(!swap)
            {
                break;
            }
        }
        for(i=0;i<k;i++)
        {
            ans.push_back(val[i]);
        }
        return ans;
        
    }
};
