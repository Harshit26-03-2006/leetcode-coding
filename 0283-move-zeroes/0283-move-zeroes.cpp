class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j = 0;
        for(int i = 0; i<nums.size(); i=i+1) {
            if(nums[i] != 0) {
                nums[j] = nums[i];
                j=j+1;
            }
        }
        while(j<nums.size()) {
            nums[j] = 0;
            j=j+1;
        }
    }
};
//T: O(n) , S: O(1)