#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    string removeStars(string s)
    {
        string stack;
        for (auto c : s)
        {
            if (c == '*')
            {
                stack.pop_back();
            }
            else
            {
                stack += c;
            }
        }

        return stack;
    }
};