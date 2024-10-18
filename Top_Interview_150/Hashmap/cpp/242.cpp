#include <string>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        unordered_set<char> set_s(s.begin(), s.end());
        unordered_set<char> set_t(t.begin(), t.end());

        unordered_map<char, int> m1;
        unordered_map<char, int> m2;

        for (char c : set_s)
            m1[c] = count(s.begin(), s.end(), c);

        for (char c : set_t)
            m2[c] = count(t.begin(), t.end(), c);

        return m1 == m2;
    }
};