class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int,int>hmap;
        int i;
        for(i=0;i<arr1.size();i++)
        {
            hmap[arr1[i]]++;
        }
        arr1.clear();
        int ele;
        int n;
        for(i=0;i<arr2.size();i++)
        {
            ele=arr2[i];
            n=hmap[ele];
            hmap.erase(ele);
            while(n)
            {
                arr1.push_back(ele);
                n--;
            }
        }
        int b=arr1.size();
        for(auto&it:hmap)
        {
            ele=it.first;
            n=it.second;
            //hmap.erase(ele);
            while(n)
            {
                arr1.push_back(ele);
                n--;
            }
            
        }
        sort(arr1.begin()+b,arr1.end());
        return arr1;
        
    }
};
