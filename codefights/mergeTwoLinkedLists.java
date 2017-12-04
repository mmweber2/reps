/*
Code for mergeTwoLinkedLists interview problem on CodeFights:
https://codefights.com/interview-practice/task/6rE3maCQwrZS3Mm2H/description

Problem statement:
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
*/

// Definition for singly-linked list:
class ListNode<T> {

   T value;
   ListNode<T> next;

   ListNode(T x) {
     value = x;
   }

    ListNode<Integer> mergeTwoLinkedLists(ListNode<Integer> l1, ListNode<Integer> l2) {
        ListNode<Integer> newList = new ListNode<Integer>(null);
        ListNode<Integer> listTail = newList;
        int next_value;
        // While both lists are non-empty, take the minimum value from each
        while (l1 != null && l2 != null) {
            if (l1.value <= l2.value) {
                next_value = l1.value;
                l1 = l1.next;
            } else {
                next_value = l2.value;
                l2 = l2.next;
            }
            // Append this value to the tail
            listTail.next = new ListNode<Integer>(next_value);
            listTail = listTail.next;
        }
        // One list is empty, so add the remainder of the other list
        if (l1 != null) {
            listTail.next = l1;
        }
        if (l2 != null) {
            listTail.next = l2;
        }
        return newList.next;
    }
}