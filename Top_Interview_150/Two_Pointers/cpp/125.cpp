#include <string>
#include <unordered_set>
#include <cctype>
#include <algorithm>

using namespace std;

class Solution
{
    unordered_set<char> __case = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                                  'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5',
                                  '6', '7', '8', '9'};

public:
    bool isPalindrome(string s)
    {
        string new_s = "";
        for (char c : s)
            if (__case.find(tolower(c)) != __case.end())
                new_s += tolower(c);

        string rev_new_s = new_s;
        reverse(rev_new_s.begin(), rev_new_s.end());

        return new_s == rev_new_s;
    }
};