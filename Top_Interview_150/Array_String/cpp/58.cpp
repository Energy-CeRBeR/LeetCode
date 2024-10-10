#include <string>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        int n = s.size();

        int i = n - 1, length = 0;
        bool flag = false;
        while (i >= 0)
        {
            if (s[i] != ' ')
            {
                length++;
                flag = true;
            }

            else if (s[i] == ' ' && flag)
            {
                break;
            }

            i++;
        }

        return length;
    }
};