/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        
        if (!head || !head->next) {
            return;
        }
        
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
//         reversing the second half of the list
        ListNode* prev = NULL;
        ListNode* current = slow;
        ListNode* next = NULL;
        
        while (current != NULL) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        
//         merging the left list and right reversed list
        ListNode* left = head;
        ListNode* right = prev;
        
        
        while (right != NULL) {
            ListNode* temp1 = left->next;
            ListNode* temp2 = right->next;
            
            left->next = right;
            right->next = temp1;
            
            left = temp1;
            right = temp2;
            
        }
        
        if (left != NULL) {
            left->next = NULL;
        }
            
        
        
        
    }
};