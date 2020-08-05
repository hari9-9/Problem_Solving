class Solution {
public:
    bool isHappy(int n) {
        
        vector<int> set;
        unordered_set<int> prev_values;
        int sum=n;
        
        while(true) {
            
            while(sum > 0) {
                set.push_back(sum % 10);
                sum=sum/10;
            }
            
            sum=0;
            for(int key: set) {
                sum += key*key;
            
            }
            
            if(sum == 1) return true;
            
            if(prev_values.count(sum) > 0) {
                return false;
            }
            else {
                prev_values.insert(sum);
            }
            
            set.clear();
        }
        return false;
    }
};
