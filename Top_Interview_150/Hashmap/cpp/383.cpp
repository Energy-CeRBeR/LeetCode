#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        unordered_map<char, int> ransomNote_case;
        for (char c : ransomNote)
            ransomNote_case[c] += 1;

        for (char c : magazine)
            if (ransomNote_case.find(c) != ransomNote_case.end())
                ransomNote_case[c]--;

        for (const auto &[key, value] : ransomNote_case)
            if (value > 0)
                return false;

        return true;
    }
};