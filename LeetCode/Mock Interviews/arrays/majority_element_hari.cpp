class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n =nums.size();
        unordered_map<int,int>hmap;
        int i;
        int maj=n/2;
        for(i=0;i<n;i++)
        {
            hmap[nums[i]]++;
            if(hmap[nums[i]]>maj)
                return nums[i];
        }
        return -1;
        
    }
};
