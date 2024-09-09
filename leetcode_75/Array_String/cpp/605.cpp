#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n)
    {
        int counter = 0;
        int size = flowerbed.size();

        if (size == 1 && flowerbed[0] == 0)
        {
            counter++;
        }

        if (size >= 2 && flowerbed[0] + flowerbed[1] == 0)
        {
            flowerbed[0] = 1;
            counter++;
        }

        for (int i = 2; i < size; ++i)
        {
            if (flowerbed[i - 2] + flowerbed[i - 1] + flowerbed[i] == 0)
            {
                flowerbed[i - 1] = 1;
                counter++;
            }
            if (counter == n)
            {
                break;
            }
        }

        if (size >= 2 && flowerbed[size - 2] + flowerbed[size - 1] == 0)
        {
            counter++;
        }

        return counter >= n ? true : false;
    }
};

int main()
{
    std::vector<int> flowerbed = {1, 0, 0, 0, 1};
    Solution solution;
    int n = 1;
    bool canPlace = solution.canPlaceFlowers(flowerbed, n);

    std::cout << "Can place flowers: " << canPlace << std::endl;
    return 0;
}