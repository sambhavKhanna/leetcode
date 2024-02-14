#include <vector>
#include <string>
using namespace std;

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>>hash = {};
    for (int i = 0; i < strs.size(); i++) {
        string s = strs[i];
        sort(s.begin(), s.end());
        if (hash.find(s) == hash.end()) {
            hash[s] = {strs[i]};
        }
        else {
            hash[s].push_back(strs[i]);
        }
    }
    vector<vector<string>> ans = {};
    for (auto it = hash.begin(); it != hash.end(); ++it) {
        ans.push_back(it->second);
    }
    return ans;
}
