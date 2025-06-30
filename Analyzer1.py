class Solution {
public:
    int findLHS(vector<int>& v) {
        unordered_map<int, int> m; // stores frequency of each element
        const int n = v.size();    // size of the input vector

        if (n == 1) return 0; // only one element, cannot form harmonious subsequence

        // Step 1: Build frequency map
        for (int num : v) {
            m[num]++; // count frequency of each number
        }

        if (m.size() == 1) return 0; // only one unique element, return 0

        int res = 0; // stores the maximum length of harmonious subsequence

        // Step 2: Check for each number if num-1 exists
        for (auto& [num, cnt] : m) {
            if (m.count(num - 1)) { // if neighbor (num-1) exists
                res = max(res, cnt + m[num - 1]); // update result if longer subsequence found
            }
        }

        return res; // final result
    }
};
