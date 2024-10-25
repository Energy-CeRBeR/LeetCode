#include <vector>

using namespace std;

class Solution
{

    bool check_answer(vector<int> &nums, int n, int target, int k)
    {
        int s = 0;
        for (int i = 0; i < k; ++i)
            s += nums[i];

        if (s >= target)
            return true;

        for (int i = k; i < n; ++i)
        {
            s -= nums[i - k];
            s += nums[i];

            if (s >= target)
                return true;
        }

        return false;
    }

public:
    int minSubArrayLen(int target, vector<int> &nums)
    {
        int n = nums.size();

        int left = 0;
        int right = n;
        while (left <= right)
        {
            int middle = (left + right) / 2;
            if (this->check_answer(nums, n, target, middle))
                right = middle - 1;
            else
                left = middle + 1;
        }

        return left <= n ? left : 0;
    }
};