class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<unsigned long long int,vector<string>> hmap;
        vector<int> v{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101};
        vector<vector<string>> res;
        for (string& s:strs) {
            unsigned long long int p = 1;
            for (char c:s) 
                p*=v[c-97];
            hmap[p].push_back(s);
            
        }
        for (auto& it:hmap) {
            res.push_back(it.second);
        }
        return res;
        
    }
};
