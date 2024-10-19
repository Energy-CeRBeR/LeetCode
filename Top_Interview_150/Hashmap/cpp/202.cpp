#include <unordered_set>

using namespace std;

class Solution
{
public:
    bool isHappy(int n)
    {
        unordered_set<int> visited;
        while (n != 1)
        {
            if (visited.find(n) != visited.end())
                return false;
            visited.insert(n);

            int new_n = 0;
            while (n > 0)
            {
                new_n += (n % 10) * (n % 10);
                n /= 10;
            }
            n = new_n;
        }

        return true;
    }
};