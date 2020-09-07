//Runtime: 996 ms
//Memory Usage: 10.2 MB

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int i,j,temp;
        int n=nums.size();
        for(i=0;i<n;i++)
        {
            for(j=0;j<n-i-1;j++)
            {
                if(nums[j]>nums[j+1])
                {
                    temp=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=temp;
                    
                }
                
            }
        }
        return nums[n-k];
        
    }
};

//Runtime: 364 ms
//Memory Usage: 10.2 MB

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int i,j,temp;
        int n=nums.size();
        for(i=0;i<k;i++)
        {
            for(j=0;j<n-i-1;j++)
            {
                if(nums[j]>nums[j+1])
                {
                    temp=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=temp;
                    
                }
                
            }
        }
        return nums[n-k];
   
        
//Runtime: 296 ms
//Memory Usage: 10.1 MB
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int i,j,temp;
        int n=nums.size();
        for(i=0;i<k;i++)
        {
            bool swap=false;
            for(j=0;j<n-i-1;j++)
            {
                
                if(nums[j]>nums[j+1])
                {
                    swap=true;
                    temp=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=temp;
                    
                }
            }
            if(!swap)
                {
                    return nums[n-k];
                }
        }
        return nums[n-k];
        
    }
};
        
       
//Runtime: 28 ms
//Memory Usage: 10.3 MB  
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n=nums.size();
        priority_queue<int>pq;
        for(int i=0;i<n;i++){
            pq.push(nums[i]);
        }
        for(int i=1;i<k;i++){
            pq.pop();
        }
        return pq.top();
    }
};      
   
