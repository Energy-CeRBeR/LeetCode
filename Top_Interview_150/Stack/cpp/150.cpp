#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

class Solution
{
public:
    int calculate(int num1, int num2, string operation)
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

    int evalRPN(vector<string> &tokens)
    {
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
                stack.push(calculate(x1, x2, token));
            }
        }

        return stack.top();
    }
};