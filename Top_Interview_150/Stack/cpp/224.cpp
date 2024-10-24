#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
#include <string>
#include <stdlib.h>

using namespace std;

class Solution
{

    vector<string> create_postfix(string s)
    {

        string valid_operations = "+-*/(";
        vector<string> operations;
        vector<string> postfix;
        unordered_map<string, int> priority = {
            {"(", -2},
            {")", -1},
            {"+", 0},
            {"-", 1},
            {"*", 2},
            {"/", 3},
        };

        bool flag = false;
        char last_symbol = '(';
        for (int i = 0; i < s.size(); ++i)
        {
            string c(1, s[i]);
            if (isdigit(s[i]))
            {
                if (flag)
                    postfix.back() += c;
                else
                    postfix.push_back(c);
                flag = true;
            }

            else if (s[i] == '(')
            {
                operations.push_back(c);
                flag = false;
            }

            else if (valid_operations.find(c) != string::npos)
            {
                if (s[i] == '-' && valid_operations.find(last_symbol) != string::npos)
                {
                    postfix.push_back("0");
                    operations.push_back(c);
                }

                else
                {
                    while (!operations.empty() && priority[c] <= priority[operations.back()])
                    {
                        postfix.push_back(operations.back());
                        operations.pop_back();
                    }
                    operations.push_back(c);
                    flag = false;
                }
            }

            else if (s[i] == ')')
            {
                while (operations.back() != "(")
                {
                    postfix.push_back(operations.back());
                    operations.pop_back();
                }
                operations.pop_back();
                flag = false;
            }

            else
                flag = false;

            if (s[i] != ' ')
                last_symbol = s[i];
        }

        while (!operations.empty())
        {
            postfix.push_back(operations.back());
            operations.pop_back();
        }

        return postfix;
    }

    int solve(int num1, int num2, string operation)
    {
        if (operation == "+")
            return num1 + num2;
        else if (operation == "-")
            return num1 - num2;
        else if (operation == "*")
            return num1 * num2;
        else if (operation == "/")
            return (int)((double)num1 / num2);
        else
            return 0;
    }

public:
    int calculate(string s)
    {
        vector<string> tokens = this->create_postfix(s);

        stack<int> stack;
        for (string &token : tokens)
        {
            if (isdigit(token[0]) || (token.length() > 1 && isdigit(token[1])))
                stack.push(stoi(token));
            else
            {
                int x2 = stack.top();
                stack.pop();
                int x1 = stack.top();
                stack.pop();
                stack.push(solve(x1, x2, token));
            }
        }

        return stack.top();
    }
};
