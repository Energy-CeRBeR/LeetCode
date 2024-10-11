#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    string intToRoman(int num)
    {
        unordered_map<int, std::string> num_map = {
            {1, "I"},
            {5, "V"},
            {4, "IV"},
            {10, "X"},
            {9, "IX"},
            {50, "L"},
            {40, "XL"},
            {100, "C"},
            {90, "XC"},
            {500, "D"},
            {400, "CD"},
            {1000, "M"},
            {900, "CM"},
        };

        string r = "";
        for (int n : {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1})
        {
            while (n <= num)
            {
                r += num_map[n];
                num -= n;
            }
        }

        return r;
    }
};