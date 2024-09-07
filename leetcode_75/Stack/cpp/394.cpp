#include <iostream>
#include <string>
#include <stack>
#include <cctype>

using namespace std;

class Solution
{
public:
    string multiplyString(const string &str, int count)
    {
        string result = "";
        for (int i = 0; i < count; ++i)
        {
            result += str;
        }
        return result;
    }

    string decodeString(string s)
    {
        stack<string> digit_stack;
        stack<string> letter_stack;
        string ans;
        char last_symbol;

        for (auto c : s)
        {
            if (isdigit(c))
            {
                if (isdigit(last_symbol))
                {
                    digit_stack.top() = digit_stack.top() + c;
                }
                else
                {
                    digit_stack.push(string(1, c));
                }
            }

            else if (c == '[')
            {
                letter_stack.push("");
            }

            else if (isalpha(c))
            {
                if (letter_stack.size() > 0)
                {
                    letter_stack.top() = letter_stack.top() + c;
                }
                else
                {
                    ans += c;
                }
            }

            else if (c == ']')
            {
                int digit = stoi(digit_stack.top());
                digit_stack.pop();
                string letter = letter_stack.top();
                letter_stack.pop();

                if (letter_stack.size() > 0)
                {
                    letter_stack.top() += this->multiplyString(letter, digit);
                }
                else
                {
                    ans += this->multiplyString(letter, digit);
                }
            }

            last_symbol = c;
        }

        return ans;
    }
};