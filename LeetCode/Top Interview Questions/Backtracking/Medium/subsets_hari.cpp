class Solution {
public:
    void solver(vector<int>& nums , int ind, int n , vector<vector<int>>& ans , vector<int>& curr)
    {
        vector<int> vect2(curr);
        ans.push_back(vect2);
        for(int i=ind;i<n;i++)
        {
            //cout<<i<<nums[i]<<endl;
            curr.push_back(nums[i]);
            solver(nums,i+1,n,ans,curr);
            curr.pop_back();            
        }
    }
    
    
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int>curr;
        solver(nums,0,nums.size(),ans,curr);
        return ans;
        
    }
};
