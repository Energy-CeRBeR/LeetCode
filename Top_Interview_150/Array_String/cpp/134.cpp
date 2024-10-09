#include <vector>

using namespace std;

class Solution
{
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
    {
        int start = 0;
        int station = 0;
        int s = 0;
        int n = gas.size();

        while (station - start < n)
        {
            s += gas[station] - cost[station];
            while (station - start < n && s < 0)
            {
                start--;
                s += gas[(start + n) % n] - cost[(start + n) % n];
            }
            station++;
        }

        if (s >= 0)
            return start >= 0 ? start : start + n;
        else
            return -1;
    }
};