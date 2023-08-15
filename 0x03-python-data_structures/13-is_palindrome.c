#ifndef LISTS_H

#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct ListNode {
    int val;
    struct ListNode *next;
} listint_t;

int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL) {
        // An empty list or a list with a single element is considered a palindrome
        return 1;
    }
    
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = NULL;
    listint_t *mid = NULL;
    
    // Find the middle of the linked list using slow and fast pointers
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }
    
    // If fast is not NULL, the list has odd number of elements
    if (fast != NULL) {
        mid = slow;
        slow = slow->next;
    }
    
    prev_slow->next = NULL; // Split the list into two halves
    
    // Reverse the second half of the linked list
    listint_t *prev = NULL;
    listint_t *curr = slow;
    listint_t *next = NULL;
    
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    
    // Compare the two halves of the linked list
    listint_t *first = *head;
    listint_t *second = prev;
    
    while (first != NULL && second != NULL) {
        if (first->val != second->val) {
            return 0; // Not a palindrome
        }
        first = first->next;
        second = second->next;
    }
    
    // Reconstruct the original linked list
    prev = NULL;
    curr = prev_slow;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    prev_slow->next = prev;
    
    // If the mid exists, reattach it to the second half
    if (mid != NULL) {
        prev_slow->next->next = mid;
    }
    
    return 1; // Palindrome
}

int main() {
    // You can create your linked list and test the function here
    return 0;
}
