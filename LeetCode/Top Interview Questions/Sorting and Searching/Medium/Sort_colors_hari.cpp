class Solution {
public:
    void sortColors(vector<int>& nums) {
        unordered_map<int ,int>hmap;
        int i;
        for(i=0;i<nums.size();i++)
        {
            hmap[nums[i]]++;
        }
        i=0;
        int f=hmap[0];
        while(f)
        {
            nums[i]=0;
            i++;
            f--;
        }
        f=hmap[1];
        while(f)
        {
            nums[i]=1;
            i++;
            f--;
        }
        f=hmap[2];
        while(f)
        {
            nums[i]=2;
            i++;
            f--;
        }
        
        
    }
};
