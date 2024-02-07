class MinStack {

    Stack<Integer> s1 = new Stack<Integer>();
    Stack<Integer> s2 = new Stack<Integer>();
    
    public MinStack() {
        
    }
    
    public void push(int val) {
        if(s2.empty()){
            s2.push(val);
        }
        else if(s2.peek()>=val){
            s2.push(val);
        }
        else{
            s2.push(s2.peek());
        }
        s1.push(val);
    }
    
    public void pop() {
        s1.pop();
        s2.pop();
    }
    
    public int top() {
        return s1.peek();
    }
    
    public int getMin() {
        return s2.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */