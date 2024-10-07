#include <vector>

using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int index = 1;
        bool flag = false;
        for (int i = 1; i < nums.size(); ++i)
        {
            if (nums[i] != nums[i - 1])
            {
                flag = false;
                nums[index] = nums[i];
                index++;
            }
            else
            {
                if (!flag)
                {
                    flag = true;
                    nums[index] = nums[i];
                    index++;
                }
            }
        }

        return index;
    }
};