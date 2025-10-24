class Solution {
public:
    int findLHS(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // Sort the numbers
        int left = 0, right = 0, maxLen = 0;
        int n = nums.size();

        while (right < n) {
            // If diff > 1, move left pointer to reduce difference
            while (nums[right] - nums[left] > 1) left++;
            
            // If diff == 1, update max length
            if (nums[right] - nums[left] == 1)
                maxLen = max(maxLen, right - left + 1);

            right++; // Expand window
        }

        return maxLen;
    }
};
