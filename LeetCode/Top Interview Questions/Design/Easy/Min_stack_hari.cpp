class MinStack {
public:
    /** initialize your data structure here. */
    stack<int>s1,s2;
    MinStack() {
        
    }
    
    void push(int x) {
        if(s1.empty())
        {
            s2.push(x);
        }
        else if(s2.top()>=x)
        {
            s2.push(x);
        }
        else 
        {
            s2.push(s2.top());
        }
        s1.push(x);
        
    }
    
    void pop() {
        if(s1.empty())return;
        s2.pop();
        s1.pop();
    }
    
    int top() {
        if(s1.empty())return -1;
        return s1.top();
    }
    
    int getMin() {
        if(s1.empty())return -1;
        return s2.top();
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
