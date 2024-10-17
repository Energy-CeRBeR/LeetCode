#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        if (nums.size() == 0)
            return 0;

        int lastNumber = INT_MIN;
        int maxCount = 1;
        int count;

        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++)
        {
            if (lastNumber == nums[i] - 1)
            {
                count++;
                lastNumber = nums[i];
            }
            else if (nums[i] > lastNumber)
            {
                lastNumber = nums[i];
                count = 1;
            }
            maxCount = max(maxCount, count);
        }
        return maxCount;
    }
};