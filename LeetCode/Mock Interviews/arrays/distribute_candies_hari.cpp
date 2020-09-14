class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        unordered_map<int,int>hmap;
        int i;
        for(i=0;i<candies.size();i++)
        {
            hmap[candies[i]]++;
        }
        int var=hmap.size();
        int tot=candies.size();
        if(var>=tot/2)
        {
            return tot/2;
        }
        else
        {
            return var;
        }
        
        
    }
};
