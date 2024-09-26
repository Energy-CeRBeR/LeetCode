#include <vector>

using namespace std;

class Solution
{

    bool check_answer(long k, vector<int> &piles, int h)
    {
        long s = 0;
        for (auto pile : piles)
        {
            s += pile / k + (int)(pile % k != 0);
        }

        return h >= s ? true : false;
    }

public:
    int minEatingSpeed(vector<int> &piles, int h)
    {
        long left = 1;
        long right = 1000000000;
        long mid;
        while (left <= right)
        {
            mid = (left + right) / 2;
            if (this->check_answer(mid, piles, h))
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }

        return left;
    }
};