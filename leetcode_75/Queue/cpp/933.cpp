#include <iostream>
#include <queue>

using namespace std;

class RecentCounter {
public:
    RecentCounter() {} 

    int ping(int t) {
        this->counter.push(t);
        int left = t - 3000;
        while (this->counter.front() < left)
        {
            this->counter.pop();
        }

        return this->counter.size();
    }

private:
    queue<int> counter;
};

int main() {
    RecentCounter rc;
    rc.ping(10); // Добавляет элемент 10 в очередь rc.counter
    return 0;
}