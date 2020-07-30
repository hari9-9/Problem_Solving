class MyHashSet {
public:
    unordered_map<int ,int> hset;
    /** Initialize your data structure here. */
    MyHashSet() {
        
    }
    
    void add(int key) {
        hset[key] = 1;
        
    }
    
    void remove(int key) {
        hset.erase(key);
        
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return hset.find(key)!= hset.end();
        
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
