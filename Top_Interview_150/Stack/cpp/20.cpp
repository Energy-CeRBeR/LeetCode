#include <string>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution
{
    unordered_map<char, char> parenthesis_1 = {
        {'(', ')'},
        {'{', '}'},
        {'[', ']'}};

    unordered_map<char, char> parenthesis_2 = {
        {')', '('},
        {'}', '{'},
        {']', '['}};

public:
    bool isValid(string s)
    {
        if (parenthesis_2.find(s[0]) != parenthesis_2.end())
            return false;

        stack<char> my_stack;
        my_stack.push(s[0]);
        int ptr = 1;
        while (ptr < s.size())
        {
            if (parenthesis_1.find(s[ptr]) != parenthesis_1.end())
                my_stack.push(s[ptr]);
            else
            {
                if (!my_stack.empty() && my_stack.top() == parenthesis_2[s[ptr]])
                    my_stack.pop();
                else
                    return false;
            }
            ptr++;
        }

        return my_stack.empty();
    }
};