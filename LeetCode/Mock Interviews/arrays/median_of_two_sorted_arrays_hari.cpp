class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int s1=nums1.size();
        int s2=nums2.size();
        int s3;
        bool flag;
        if((s1+s2)%2 !=0)
        {
            s3=((s1+s2)/2);
            flag=true;
        }
        else
        {
            s3=(int)((s1+s2)/2)+1;  // Concern
            flag=false;
        }
        //cout<<s3<<" "<<flag<<endl;
        //return s3;
        int i=0;
        int j=0;
        int k=0;
        vector<int>ans;
        while(i<=s3 && j<s1 && k<s2)
        {
            if(nums1[j]<nums2[k])
            {
                ans.push_back(nums1[j]);
                j++;
            }
            else
            {
                ans.push_back(nums2[k]);
                k++;
            }
            i++;
        }
        while(i<=s3 && j<s1)
        {
            ans.push_back(nums1[j]);
            j++;
            i++;
        }
        while(i<=s3 && k<s2)
        {
            ans.push_back(nums2[k]);
            k++;
            i++;
        }      
        // for(i=0;i<ans.size();i++)
        // {
        //     cout<<ans[i]<<" ";
        // }
        //cout<<endl;
        if(flag)
        {
            return ans[s3];
        }
        else
        {
            //cout<<ans[s3-1]<<" "<<ans[s3-2]<<" "<<((ans[s3-2]+ans[s3-1])/2);
            return((float)(ans[s3-2]+ans[s3-1])/2);
        }
        
    }
};
