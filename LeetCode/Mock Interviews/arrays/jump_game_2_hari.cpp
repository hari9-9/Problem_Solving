class Solution {
public:
    void jumper(vector<int>& nums , vector<int>& steps , int curr , int s , int target, int k)
    {
        if(curr == target)
        {
            //cout<<s<<endl;
            steps.push_back(s);
            return;
        }
        
        for(int i =nums[curr];i>0;i--)
        {
            if(curr+i<=target && i!=0)
            {
                jumper(nums,steps,curr+i,s+1,target , k);   
            }
        }
    }
    
    
    int jump(vector<int>& nums) {
        
        vector<int>steps;
        int k=INT_MAX;
        int target=nums.size()-1;
        jumper(nums,steps,0,0,target,k);
        return *min_element(steps.begin(), steps.end());
        
        
    }
};
