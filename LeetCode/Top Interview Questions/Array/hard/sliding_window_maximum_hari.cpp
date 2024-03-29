// https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& arr, int k) {
        std::deque<int> Qi(k);
        int i;
        int n =arr.size();
        std::vector<int> ints;
        for(i=0;i<k;++i)
        {
            while ((!Qi.empty()) && arr[i] >=arr[Qi.back()])
                Qi.pop_back();
 
        
            Qi.push_back(i);
        }
        for (; i < n; ++i)
        {
            //cout << arr[Qi.front()] << " ";
            ints.push_back(arr[Qi.front()]);
            while ((!Qi.empty()) && Qi.front() <=i - k)
                Qi.pop_front();

            while ((!Qi.empty()) && arr[i] >=arr[Qi.back()])
                Qi.pop_back();

        Qi.push_back(i);
    }
 
    //cout << arr[Qi.front()];
    ints.push_back(arr[Qi.front()]);
    return ints;
    }
};
