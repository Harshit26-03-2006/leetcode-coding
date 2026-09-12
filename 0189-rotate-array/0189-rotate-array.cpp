class Solution {
public:
    void rotate(vector<int>& nums, int k) {
       int n = nums.size();

       int count = 0;
       for (int i = 0; count < n; i++) {
            int idx = i;
            int curr = nums[idx];
            do {
                int next = nums[(idx + k) % n];
                nums[(idx + k) % n] = curr;
                curr = next;
                idx = (idx + k) % n;
                count = count + 1;
            } while(idx != i);
       }
    }
};