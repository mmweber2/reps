// Solution for CodeFights rearrangeLastN
// https://codefights.com/interview-practice/task/5vcioHMkhGqkaQQYt/description

/*
Problem statement:
Note: Try to solve this task in O(list size) time using O(1) additional space,
  since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n,
  move the last n list nodes to the beginning of the linked list.

Guaranteed constraints:
0 <= n <= list size

*/

// ListNode definition from problem statement
class ListNode<T> {
   ListNode(T x) {
     value = x;
   }
   T value;
   ListNode<T> next;

   ListNode<Integer> rearrangeLastN(ListNode<Integer> l, int n) {
       if (n == 0) {
           // Move the last 0 elements means don't change anything
           return l;
       }
       // Move a fast pointer ahead n nodes
       ListNode<Integer> fast = l;
       for (int i = 0; i < n; i++) {
           fast = fast.next;
       }
       if (fast == null) {
           // n is the length of list, so don't change anything
           return l;
       }
        // The first node in the subsequence to move
       ListNode<Integer> mid = l.next;
       // The last node before the subsequence to move
       ListNode<Integer> slow = l;
       while (fast.next != null) {
           fast = fast.next;
           mid = mid.next;
           slow = slow.next;
       }
       // Attach the head of the original list to the end of the subsequence
       fast.next = l;
       // Remove pointer to mid from the end of the new list
       slow.next = null;
       // mid now points to the head of the rearranged list
       return mid;
    }
}