#include <vector>
#include <stack>

using namespace std;

class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        int n = temperatures.size();
        vector<int> result(n, 0);

        stack<pair<int, int>> st;
        st.push({temperatures[0], 0});
        for (int i = 1; i < n; ++i)
        {
            while (!st.empty() && st.top().first < temperatures[i])
            {
                result[st.top().second] = i - st.top().second;
                st.pop();
            }

            st.push({temperatures[i], i});
        }

        return result;
    }
};