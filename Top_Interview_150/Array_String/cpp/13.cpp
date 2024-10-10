#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        unordered_map<char, int> roman_values = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}};

        unordered_map<string, int> special_numbers = {
            {"IV", 4},
            {"IX", 9},
            {"XL", 40},
            {"XC", 90},
            {"CD", 400},
            {"CM", 900}};

        int n = s.size(), int_result = 0, i = 0;
        while (i < n)
        {
            auto data = special_numbers.find(s.substr(i, 2));
            if (i + 1 < n && data != special_numbers.end())
            {
                int_result += data->second;
                i += 2;
            }
            else
            {
                int_result += roman_values[s[i]];
                i++;
            }
        }

        return int_result;
    }
};