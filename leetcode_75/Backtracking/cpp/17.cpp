#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
    unordered_map<char, string> converter = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}};

    vector<string> backtracking(string combination, string digits, vector<string> &result)
    {
        if (digits.empty())
        {
            result.push_back(combination);
        }
        else
        {
            for (auto c : this->converter[digits[0]])
            {
                this->backtracking(combination + c, digits.substr(1, digits.size() - 1), result);
            }
        }

        return result;
    }

public:
    vector<string> letterCombinations(string digits)
    {
        if (digits.empty())
        {
            return {};
        }

        vector<string> pattern;

        return this->backtracking("", digits, pattern);
    }
};