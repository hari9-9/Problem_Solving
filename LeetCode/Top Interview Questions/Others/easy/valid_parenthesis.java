class Solution {
    public boolean isValid(String s) {
        if(s.length()%2!=0){
            return false;
        }
        Stack<Character> stack = new Stack<Character>();
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(c=='('||c=='{'||c=='['){
                stack.push(c);
            }
            else{
                if(stack.isEmpty()){
                    return false;
                }
                char out = stack.pop();
                if(c==')' && out=='(') continue;
                else if(c=='}' && out=='{') continue;
                else if(c==']' && out=='[') continue;
                else{
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}