#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<int> asteroidCollision(vector<int> &asteroids)
    {
        vector<int> stack;
        for (auto ast : asteroids)
        {
            int cur = ast;
            stack.push_back(cur);
            if (stack.size() >= 2)
            {
                int prev = stack[stack.size() - 2];
                while (cur < 0 && prev > 0)
                {
                    if (abs(cur) > abs(prev))
                    {
                        stack[stack.size() - 2] = cur;
                        stack.pop_back();
                    }
                    else if (abs(cur) == (abs(prev)))
                    {
                        stack.pop_back();
                        stack.pop_back();
                    }
                    else
                    {
                        stack.pop_back();
                    }

                    if (stack.size() < 2)
                    {
                        break;
                    }

                    cur = stack[stack.size() - 1];
                    prev = stack[stack.size() - 2];
                }
            }
        }

        return stack;
    }
};