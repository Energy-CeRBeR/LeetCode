#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <sstream>

using namespace std;

class Solution
{
    vector<string> splitString(const string &str)
    {
        vector<string> words;
        stringstream ss(str);
        string word;

        while (getline(ss, word, ' '))
        {
            words.push_back(word);
        }

        return words;
    }

public:
    bool wordPattern(string pattern, string s)
    {
        unordered_map<char, string> dct;
        vector<string> words = this->splitString(s);

        if (pattern.size() != words.size())
            return false;

        unordered_set<string> added_words;
        for (int i = 0; i < pattern.size(); ++i)
        {
            if (dct.find(pattern[i]) == dct.end())
            {
                if (added_words.find(words[i]) == added_words.end())
                {
                    dct[pattern[i]] = words[i];
                    added_words.insert(words[i]);
                }
                else
                    return false;
            }
            else if (words[i] != dct[pattern[i]])
                return false;
        }

        return true;
    }
};