#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1)
            return s;

        int n = s.size();
        vector<string> components(numRows, "");

        int j = 0;
        int d = 1;
        for (int i = 0; i < n; ++i)
        {
            components[j] += s[i];

            if (j == 0)
                d = 1;
            else if (j == numRows - 1)
                d = -1;
            j += d;
        }

        string result = "";
        for (int i = 0; i < numRows; ++i)
        {
            result += components[i];
        }

        return result;
    }
};