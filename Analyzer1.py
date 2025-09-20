class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> freq;
        int maxLen = 0;

        for (int num : nums) {
            int cnt = ++freq[num];  // increment frequency

            if (freq.count(num - 1)) {
                maxLen = max(maxLen, cnt + freq[num - 1]);
            }
            if (freq.count(num + 1)) {
                maxLen = max(maxLen, cnt + freq[num + 1]);
            }
        }

        return maxLen;
    }
};
