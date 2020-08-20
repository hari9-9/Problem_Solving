class Solution {
public:
    vector<int> topKFrequent(vector<int>& arr, int k) {
        unordered_map<int, int> um;
        int n = arr.size();
    for (int i = 0; i < n; i++) 
        um[arr[i]]++;  
    vector<int> freq[n + 1]; 
    for (int i = 0; i < n; i++) { 
        int f = um[arr[i]]; 
        if (f != -1) { 
            freq[f].push_back(arr[i]); 
            um[arr[i]] = -1; 
        } 
    }  
    int count = 0; 
    vector<int >ans;
    for (int i = n; i >= 0; i--) { 
        for (int x : freq[i]) { 
            ans.push_back(x);
            cout << x << " "; 
            count++; 
            if (count == k) 
                return ans; 
        } 
    } 
        return ans;
        
    }
};
