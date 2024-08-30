#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int maxOperations(vector<int> &nums, int k)
    {
        sort(nums.begin(), nums.end());
        int left = 0;
        int right = nums.size() - 1;
        int counter = 0;

        while (left < right)
        {
            if (nums[left] + nums[right] == k)
            {
                counter++;
                left++;
                right--;
            }
            else
            {
                nums[left] + nums[right] < k ? left++ : right--;
            }
        }

        return counter;
    }
};