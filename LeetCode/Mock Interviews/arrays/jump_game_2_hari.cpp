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


// Second attempt

class Solution {
public:
    int jump(vector<int>& nums) {
        int n= nums.size();
        int i,j;
        int jumps[n];
        if(n==0 || nums[0]==0)
        {
            return 0;
        }
        jumps[0]=0;
        for(i=1;i<n;i++)
        {
            jumps[i]=INT_MAX;
            for(j=0;j<i;j++)
            {
                if(i<=j+nums[j] && jumps[j]!=INT_MAX)
                {
                    jumps[i] = min(jumps[i] , jumps[j]+1);
                    break;
                }
            }
        }
        
        return jumps[n-1];
    }
};
