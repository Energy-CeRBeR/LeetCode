#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    bool containsNearbyDuplicate(vector<int> &nums, int k)
    {
        unordered_map<int, int> dct;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (dct.find(nums[i]) != dct.end())
                if (i - dct[nums[i]] <= k)
                    return true;
            dct[nums[i]] = i;
        }

        return false;
    }
};