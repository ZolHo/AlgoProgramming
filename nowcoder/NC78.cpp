//逆转链表
#include <cstdio>
#include <iostream>
#include <stack>
using namespace std;
struct ListNode {
    int val;
    struct ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {
    }
};
class Solution {
   public:
    ListNode* ReverseList(ListNode* pHead) {
        if (pHead == nullptr) return pHead;
        stack<ListNode*> s;
        ListNode* temp;
        while (pHead->next != nullptr && pHead->next != pHead) {
            s.push(pHead);
            pHead = pHead->next;
        }
        temp = pHead;
        while (s.size() > 0) {
            temp->next = s.top();
            s.pop();
            temp = temp->next;
        }
        temp->next = nullptr;
        return pHead;
    }
};

int main() {
    ListNode* p = (ListNode*)alloca(sizeof(ListNode));
    p->val = 0;
    ListNode* temp;
    temp = p;
    for (int i = 1; i < 4; i++) {
        ListNode* t = new ListNode(i);
        p->next = t;
        p = p->next;
    }
    Solution s;
    cout << p->val << " " << temp->next << " " << temp->next->next << endl;
    temp = s.ReverseList(temp);
    while (temp->next != nullptr) {
        cout << "yes " << temp->val << endl;
        temp = temp->next;
    }
}