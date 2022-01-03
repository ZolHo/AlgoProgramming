//设计LRU缓存结构
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;


class deLinkedListNode {
   public:
    deLinkedListNode *prev, *next;
    int data,key;
    deLinkedListNode(int k, int d) : data(d), key(k){};

};

class Solution {
   public:
    /**
     * lru design
     * @param operators int整型vector<vector<>> the ops
     * @param k int整型 the k
     * @return int整型vector
     */
    vector<int> LRU(vector<vector<int> >& operators, int k) {
        this->m_cap = k;
        this->m_usecap = 0;
        this->m_Head = new deLinkedListNode(0,0);
        this->m_End = new deLinkedListNode(0,0);
        this->m_Head->next = this->m_End;
        this->m_End->prev = this->m_Head;
        vector<int> ans = {};

        for (auto code : operators) {
            switch (code[0])
            {
            case 2:
                ans.push_back(getData(code[1]));
                break;
            case 1:
                setData(code[1], code[2]);
                break;
            default:
                break;
            }
        }
        return ans;
    }

    void setData(const int &key, const int &value) {
        auto findIt = this->m_nodemap.find(key);
        if (findIt == this->m_nodemap.end()) {
            deLinkedListNode *temp = new deLinkedListNode(key, value);
            if (this->m_cap <= this->m_usecap) {
                removeLast();
            }
            insertFrist(temp);
            this->m_nodemap[key] = temp;
        } else {
            insertFrist(removeNode(findIt->second));
            findIt->second->data = value;
        }

    }

    int getData (const int &key) {
        auto findIt = this->m_nodemap.find(key);
        if (findIt == this->m_nodemap.end()) {
            return -1;
        } else {
            insertFrist(removeNode(findIt->second));
            return findIt->second->data;
        }
    }

    void insertFrist(deLinkedListNode *p) {
        p->next = this->m_Head->next;
        p->prev = this->m_Head;
        p->next->prev = p;
        this->m_Head->next = p;
        this->m_usecap += 1;
    }

    void removeLast() {
        this->m_nodemap.erase(this->m_End->prev->key);
        delete removeNode (this->m_End->prev);
    }

    deLinkedListNode* removeNode(deLinkedListNode *p) {
        p->prev->next = p->next;
        p->next->prev = p->prev;
        this->m_usecap -= 1;
        return p;
    }

    private:
    deLinkedListNode *m_Head, *m_End;
    int m_cap, m_usecap;
    unordered_map<int, deLinkedListNode* > m_nodemap;
};