
class Solution {

    public void del(Stack<Integer> s , int n , int curr){
        if(s.empty() || curr==n){
            return;
        }
        int temp = s.pop();
        del(s,n,curr+1);
        if(curr!=n/2){
            s.push(temp);
        }
    }
    // Function to delete middle element of a stack.
    public void deleteMid(Stack<Integer> s) {
        // code here
        del(s,s.size(),0);
    }
}
