#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution
{
public:
    bool closeStrings(string word1, string word2)
    {
        int l1 = word1.size();
        int l2 = word2.size();
        if (l1 != l2)
        {
            return false;
        }

        unordered_set<char> s1(word1.begin(), word1.end());
        unordered_set<char> s2(word2.begin(), word2.end());
        if (s1 != s2)
        {
            return false;
        }

        vector<int> d1;
        for (auto c : s1)
        {
            int count = std::count(word1.begin(), word1.end(), c);
            d1.push_back(count);
        }
        sort(d1.begin(), d1.end());

        vector<int> d2;
        for (auto c : s2)
        {
            int count = std::count(word2.begin(), word2.end(), c);
            d2.push_back(count);
        }
        sort(d2.begin(), d2.end());

        return d1 == d2;
    }
};