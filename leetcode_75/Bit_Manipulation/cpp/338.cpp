#include <vector>

using namespace std;

class Solution
{

    int unit_counter(int num)
    {
        int count = 0;
        while (num > 0)
        {
            count += (num % 2 == 1);
            num /= 2;
        }
        return count;
    }

public:
    vector<int> countBits(int n)
    {
        vector<int> result;
        for (int x = 0; x <= n; ++x)
        {
            result.push_back(this->unit_counter(x));
        }

        return result;
    }
};