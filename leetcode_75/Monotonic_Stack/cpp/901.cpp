#include <stack>

using namespace std;

class StockSpanner
{
    stack<pair<int, int>> st;

public:
    StockSpanner()
    {
    }

    int next(int price)
    {
        int counter = 1;
        while (!this->st.empty() && this->st.top().first <= price)
        {
            counter += this->st.top().second;
            this->st.pop();
        }
        this->st.push({price, counter});

        return counter;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */