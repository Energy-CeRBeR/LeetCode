#include <string>
#include <queue>

using namespace std;

class Solution
{
public:
    string predictPartyVictory(string senate)
    {
        int n = senate.size();
        queue<int> queue_R;
        queue<int> queue_D;

        for (int i = 0; i < n; ++i)
        {
            if (senate[i] == 'R')
            {
                queue_R.push(i);
            }
            else
            {
                queue_D.push(i);
            }
        }

        while (queue_R.size() > 0 && queue_D.size() > 0)
        {
            int r_index = queue_R.front();
            queue_R.pop();
            int d_index = queue_D.front();
            queue_D.pop();

            if (r_index < d_index)
            {
                queue_R.push(r_index + n);
            }
            else
            {
                queue_D.push(d_index + n);
            }
        }

        return queue_R.size() > 0 ? "Radiant" : "Dire";
    }
};