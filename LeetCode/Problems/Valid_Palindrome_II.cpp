// Runtime: 116 ms, faster than 71.59% of C++ online submissions for Valid Palindrome II.
// Memory Usage: 45.1 MB, less than 5.12% of C++ online submissions for Valid Palindrome II.

class Solution {
public:
    int func(string s, int flag){
        auto l = s.length();
        auto i = s.begin();
        auto j = s.rbegin();

        int k=0;

        while(k<(l/2))
        {
            // flag=1 -> check palindrome
            // flag=2 -> get mis-matching index
            if(flag==1) {
                if (*i != *j)
                    return 0;
            }
            else {
                if (*i != *j)
                    return k;
            }
            i++;
            j++;
            k++;
        }

        return 1;
    }

    string pop_from_index(string s, int index){
        string ns;
        for (int i = 0; i < s.length(); i++) {
            if (i!=index)
                ns.push_back(s[i]);
        }
        return ns;
    }
    
    bool validPalindrome(string s) {

        int l = s.length();

        int b = func(s, 1);
        if(b==1) return true;

        int m = func(s, 2);

        string s1 = pop_from_index(s, m);
        b = func(s1, 1);
        if(b==1) return true;

        string s2 = pop_from_index(s, l-m-1);
        b = func(s2, 1);
        if(b==1) return true;

        return false;       
    }
};
