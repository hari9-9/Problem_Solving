class Solution {
public:
    bool isValid(string s) {
        int l=s.size();
        char stack[l+1];
        int n=-1;
        int i;
        for(i=0;i<l;i++)
        {
            if(s[i]=='(' || s[i]=='{' || s[i]=='[')
            {
                n++;
                stack[n]=s[i];
                cout<<n;
            }
            else
            {
                if(n==-1)
                {
                    return false;
                }
                else if((s[i]==')' && stack[n]=='(') || (s[i]=='}' && stack[n]=='{') || (s[i]==']' && stack[n]=='['))
                    n--;
                else
                {
                    return false;
                }
            }
        }
        if(n==-1)
        {
            return true;
        }
        else
            return false;
        
    }
};
