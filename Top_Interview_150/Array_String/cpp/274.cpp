#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int hIndex(vector<int> &citations)
    {
        sort(citations.begin(), citations.end());
        int n = citations.size();

        int j = 0;
        int h = -1;
        for (int i = 0; i < 1000; ++i)
        {
            while (j < n && citations[j] < i)
            {
                j++;
            }

            if (n - j >= i)
            {
                h = i;
            }
        }

        return h;
    }
};