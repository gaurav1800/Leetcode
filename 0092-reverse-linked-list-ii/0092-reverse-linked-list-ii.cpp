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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        
        if (!head || !head->next || left == right) {
            return head;
        }
        
//         ListNode *current = new ListNode(0, head);
        
//         ListNode *result = current;
        
//         int counter = 1;
        
//         while (counter+1 != left) {
//             current = current->next;
//             counter++;
//         }
        
//         ListNode *prev = current;
//         current = current->next;
//         ListNode *next = current->next;
        
//         while (current != nullptr && counter != right) {
//             next = current->next;
//             current->next = prev;
//             prev = current;
//             current = next;
//             counter++;
//         }
        
//         return result->next;
        
        ListNode dummy(0); // Create a dummy node
        dummy.next = head;
        ListNode* prev = &dummy;

        // Move prev to the node just before the left-th node
        for (int i = 1; i < left; ++i) {
            prev = prev->next;
        }

        // Reverse the sublist between left and right
        ListNode* current = prev->next;
        ListNode* next = nullptr;
        ListNode* reverse_tail = current; // The tail of the reversed sublist
        
        for (int i = left; i < right; ++i) {
            next = current->next;
            current->next = next->next;
            next->next = prev->next;
            prev->next = next;
        }

        // Return the new head
        return dummy.next;
        
        
        
    }
};