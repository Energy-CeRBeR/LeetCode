#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    string reverseVowels(string s)
    {
        string vowels = "aeiouAEIOU";
        int ptr1 = 0;
        int ptr2 = s.size() - 1;
        while (ptr1 < ptr2)
        {
            while (vowels.find(s[ptr1]) == vowels.npos || vowels.find(s[ptr2]) == vowels.npos)
            {
                if (vowels.find(s[ptr1]) == vowels.npos)
                {
                    ptr1++;
                }
                if (vowels.find(s[ptr2]) == vowels.npos)
                {
                    ptr2--;
                }
                if (ptr1 >= ptr2)
                {
                    return s;
                }
            }
            swap(s[ptr1], s[ptr2]);
            ptr1++;
            ptr2--;
        }

        return s;
    }
};