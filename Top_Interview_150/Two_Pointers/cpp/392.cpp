#include <string>

using namespace std;

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        if (s.empty())
            return true;

        int n = s.size();
        int ptr_s = 0;
        for (char c : t)
        {
            if (c == s[ptr_s])
                ptr_s++;

            if (ptr_s == n)
                return true;
        }

        return false;
    }
};