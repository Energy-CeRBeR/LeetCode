#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class SmallestInfiniteSet
{

    priority_queue<int, vector<int>, greater<int>> heap;
    unordered_set<int> set_heap;
    int next_smallest = 1;

public:
    SmallestInfiniteSet()
    {
    }

    int popSmallest()
    {
        int smallest;

        if (!this->heap.empty())
        {
            smallest = this->heap.top();
            this->heap.pop();
            this->set_heap.erase(smallest);

            return smallest;
        }

        smallest = this->next_smallest;
        this->next_smallest++;

        return smallest;
    }

    void addBack(int num)
    {
        if (num < this->next_smallest && this->set_heap.find(num) == this->set_heap.end())
        {
            this->heap.push(num);
            this->set_heap.insert(num);
        }
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */