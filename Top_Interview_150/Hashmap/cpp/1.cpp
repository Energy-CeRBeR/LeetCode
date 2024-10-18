#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> numMap;
        int n = nums.size();
        for (int i = 0; i < n; ++i)
            numMap[nums[i]] = i;

        for (int i = 0; i < n; ++i)
        {
            int complect = target - nums[i];
            if (numMap.find(complect) != numMap.end() && numMap[complect] != i)
                return {i, numMap[complect]};
        }

        return {};
    }
};