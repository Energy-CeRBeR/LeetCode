#include <stack>
#include <algorithm>

using namespace std;

class MinStack
{
    stack<pair<int, int>> st;

public:
    MinStack()
    {
    }

    void push(int val)
    {
        if (this->st.empty())
            this->st.push({val, val});
        else
            this->st.push({val, min(val, this->st.top().second)});
    }

    void pop()
    {
        this->st.pop();
    }

    int top()
    {
        return this->st.top().first;
    }

    int getMin()
    {
        return this->st.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */