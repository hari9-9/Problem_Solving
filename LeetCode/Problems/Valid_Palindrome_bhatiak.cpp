// Runtime: 8 ms, faster than 87.30% of C++ online submissions for Valid Palindrome.
// Memory Usage: 8.1 MB, less than 48.07% of C++ online submissions for Valid Palindrome.

class Solution {
public:
    
    string cleanedString(string s){
        string ns;
        for (auto i = s.begin(); i != s.end(); ++i) {
            if(((int)*i >= 97 && (int)*i <= 122) || ((int)*i >= 48 && (int)*i <= 57))
                ns.push_back(*i);
            if((int)*i >= 65 && (int)*i <= 90)
                ns.push_back((char)((int)*i+32));
        }
        return ns;
    }
    
    bool isPalindrome(string s) {
        
        s = cleanedString(s);
        
        auto l = s.length();
        auto i = s.begin();
        auto j = s.rbegin();

        int k=0;

        while(k<(l/2))
        {
            if (*i != *j)  
                return false;
            i++;
            j++;
            k++;
        }

        return true;        
    }
};
