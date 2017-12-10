// Solution for CodeFights reverseNodesInKGroups
// https://codefights.com/interview-practice/task/XP2Wn9pwZW6hvqH67/description

/*
Note: Your solution should have O(n) time complexity, where n is the number of element in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list.
k is a positive integer that is less than or equal to the length of l.
If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.
*/

// ListNode definition from problem statement
class ListNode<T> {
   ListNode(T x) {
     value = x;
   }
   T value;
   ListNode<T> next;

   ListNode<Integer> reverseNodesInKGroups(ListNode<Integer> l, int k) {
    if (k == 1) {
        // No reversal needed
        return l;
    }
    int listLength = 0;
    ListNode<Integer> current = l;
    // Get length of list
    while (current != null) {
        listLength++;
        current = current.next;
    }
    current = l;
    // The tail of the last chunk we traversed
    ListNode<Integer> tail = null;
    // Do listLength / k reversals
    for (int i = 0; i < listLength / k; i++) {
        ListNode<Integer> prevNode = null;
        ListNode<Integer> localHead = current;
        
        for (int j = 0; j < k; j++) {
            ListNode<Integer> nextNode = current.next;
            current.next = prevNode;
            prevNode = current;
            current = nextNode;
        }
        
        // After traversal, prevNode points to the new head of the sublist,
        // which should either head the full list or be attached to the end
        // of the previous sublist
        if (i == 0) {
            l = prevNode;
        } else {
            tail.next = prevNode;
        }
        // The new tail is the value that headed the sublist before reversing
        tail = localHead; 
    }
    // When the reversals are done, connect tail to the remaining list (if any)
    tail.next = current;
    return l;
    }
}