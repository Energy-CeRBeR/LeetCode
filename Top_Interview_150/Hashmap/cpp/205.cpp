#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution
{
public:
    bool isIsomorphic(string s, string t)
    {
        unordered_set<char> set_s(s.begin(), s.end());
        unordered_set<char> set_t(t.begin(), t.end());

        int n = s.size();

        vector<int> v1;
        vector<int> v2;
        for (char c : set_s)
            v1.push_back(count(s.begin(), s.end(), c));

        for (char c : set_t)
            v2.push_back(count(t.begin(), t.end(), c));

        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());

        if (v1 != v2)
            return false;

        unordered_map<char, char> dct;
        for (char c : set_s)
            dct[c] = c;

        for (int i = 0; i < n; ++i)
            if (s[i] != t[i])
                dct[s[i]] = t[i];

        string new_s;
        for (char c : s)
            new_s += dct[c];

        return new_s == t;
    }
};