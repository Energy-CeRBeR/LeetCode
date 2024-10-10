#include <vector>

using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        int left = 0, right = height.size() - 1;
        int left_max = height[left], right_max = height[right];
        int count_water = 0;

        while (left < right)
        {
            if (left_max < right_max)
            {
                left += 1;
                left_max = max(left_max, height[left]);
                count_water += left_max - height[left];
            }
            else
            {
                right -= 1;
                right_max = max(right_max, height[right]);
                count_water += right_max - height[right];
            }
        }

        return count_water;
    }
};
