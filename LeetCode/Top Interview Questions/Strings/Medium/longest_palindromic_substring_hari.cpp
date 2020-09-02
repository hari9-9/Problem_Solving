class Solution {
public:
    string longestPalindrome(string s) {
        if(s.length()==1)
        {
            return s;
        }
        if(s.length()==2)
        {
            if(s[0]==s[1])
            {
                return s;
            }
            else
            {
                return s.substr(0,1);
            }
        }
        if(s.length()<1)
        {
            return "";
        }
        int start=0;
        int end=0;
        int i=0;
        for(i=0;i<s.length();i++)
        {
            int l1=middle(s,i,i);
            int l2=middle(s,i,i+1);
            int len = l1>l2? l1:l2;
            if(len>end-start)
            {
                start = i - (len - 1) / 2;
                end = i + len / 2;  
            }
            
        }
        return s.substr(start,end+1);
        
    }
    
    int middle(string s , int left , int right)
    {
        int l=left;
        int r=right;
        while(l>=0 && r<s.length() && s[l]==s[r])
        {
            l--;
            r++;
        }
        return r-l-1;
    }
};
