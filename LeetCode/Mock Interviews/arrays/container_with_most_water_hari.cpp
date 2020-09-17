class Solution {
public:
    int maxArea(vector<int>& height) {
        int start=0;
        int ans=0;
        int n=height.size();
        int stop =n-1;
        while(start<stop)
        {
            ans=max(ans,min(height[start],height[stop])*(stop-start));
            if(height[start]>=height[stop])
            {
                stop--;
            }
            else
            {
                start++;
            }
        }
        return ans;
    }
};
