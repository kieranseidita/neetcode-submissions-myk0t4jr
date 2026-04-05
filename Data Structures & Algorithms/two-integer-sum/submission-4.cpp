class Solution {
    public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //Step 1: Define Integers i & j and also define a vector
        int i, j;

        vector<int> new_nums;
         
        //Step 2: Create a double for loop to go through
        for(i = 0; i < nums.size(); i++){
            for(j = i + 1; j < nums.size(); j++){
                if(nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};
