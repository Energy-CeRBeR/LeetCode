#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    bool increasingTriplet(vector<int> &nums)
    {
        long int first = 10000000000000000;
        long int second = 10000000000000000;
        for (auto num : nums)
        {
            if (num <= first)
            {
                first = num;
            }
            else if (first < num && num <= second)
            {
                second = num;
            }
            else if (num > second)
            {
                return true;
            }
        }

        return false;
    }
};
