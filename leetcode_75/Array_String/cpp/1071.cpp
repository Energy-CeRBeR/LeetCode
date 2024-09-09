#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    string gcdOfStrings(string str1, string str2)
    {

        if (str1.length() < str2.length())
        {
            return this->gcdOfStrings(str2, str1);
        }
        else if (str1.find(str2) != 0)
        {
            return "";
        }
        else if (str2 == "")
        {
            return str1;
        }
        else
        {
            return this->gcdOfStrings(str1.substr(str2.length()), str2);
        }
    }
};
