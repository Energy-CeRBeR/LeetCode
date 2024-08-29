#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        int l1 = s.size();
        int l2 = t.size();
        if (l1 > l2)
        {
            return false;
        }
        if(l1 == 0)
        {
            return true;
        }

        int j = 0;
        for (int i = 0; i < l2; ++i)
        {
            if (t[i] == s[j])
            {
                j += 1;
            }
            if (j == l1)
            {
                return true;
            }
        }

        return false;
    }
};