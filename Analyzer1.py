class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> freq;
        int maxLen = 0;

        // Count frequencies of each number
        for (int num : nums) {
            freq[num]++;
        }

        // Check pairs of consecutive numbers
        for (auto& [num, count] : freq) {
            if (freq.count(num + 1)) {
                maxLen = max(maxLen, count + freq[num + 1]);
            }
        }

        return maxLen;
    }
};
