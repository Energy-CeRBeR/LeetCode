#include <vector>

using namespace std;

class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        int n = nums.size();
        k %= n;
        vector<int> offset(n, 0);
        for (int i = 0; i < n - k; ++i)
        {
            offset[i] = nums[i];
        }

        int count = 0;
        int i = n - k;
        while (count < k)
        {
            nums[count] = nums[i];
            count++;
            i++;
        }

        for (int i = k; i < n; ++i)
        {
            nums[i] = offset[i - k];
        }
    }
};