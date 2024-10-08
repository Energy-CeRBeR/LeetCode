#include <vector>
#include <unordered_map>
#include <random>

using namespace std;

class RandomizedSet
{
    unordered_map<int, int> hash_idx;
    vector<int> data;
    random_device rd;
    mt19937 gen;

public:
    RandomizedSet()
    {
    }

    bool insert(int val)
    {
        if (this->hash_idx.find(val) == hash_idx.end())
        {
            this->data.push_back(val);
            this->hash_idx[val] = data.size() - 1;
            return true;
        }
        return false;
    }

    bool remove(int val)
    {
        auto idx_data = this->hash_idx.find(val);
        if (idx_data != this->hash_idx.end())
        {
            int idx = idx_data->second;
            this->data[idx] = this->data.back();
            this->hash_idx[this->data.back()] = idx;

            this->data.pop_back();
            this->hash_idx.erase(val);
            return true;
        }
        return false;
    }

    int getRandom()
    {
        uniform_int_distribution<> distrib(0, data.size() - 1);
        return data[distrib(gen)];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */