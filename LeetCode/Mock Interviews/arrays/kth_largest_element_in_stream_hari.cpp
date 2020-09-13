class KthLargest {
public:
    vector<int> num;
    int l;
    KthLargest(int k, vector<int>& nums) {
        l=k;
        num=nums;
        sort(num.begin(),num.end());
    }
    
    int add(int val) {
        //finding spot
        int i;
        // for(i=0;i<num.size();i++)
        // {
        //     cout<<num[i]<<" ";
        // }
        // cout<<endl;
        
        num.push_back(0);
        for (i = num.size() - 2; (i >= 0 && num[i] > val); i--) 
            num[i + 1] = num[i]; 
  
        num[i + 1] = val;
        return(num[num.size()-l]);
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */



//priority_Queue implementation

class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> pq;
    int k;
    KthLargest(int k, vector<int>& nums) {
        this->k=k;
        for(int i=0;i<nums.size();i++)
        {
            if(pq.size()>=k)
            {
                if(nums[i]>pq.top())
                {
                    pq.pop();
                    pq.push(nums[i]);
                }
            }
            else
                pq.push(nums[i]);
            
        }
        
    }
    
    int add(int val) {
        if(pq.size()==0 || pq.size()<k)
            pq.push(val);
       else if(val>pq.top())
        {
            pq.pop();
            pq.push(val);
        }
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
