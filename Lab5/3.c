#include <stdio.h>
#include <stdlib.h>

// structure for a node in circular linked list
struct Node {
    int data;
    struct Node* next;
};

// Function to find the only person left after one in every m-th node is killed in a circle of n nodes
// The 1st monkey's label starts with 0 as an index
void monkeyKing(int m, int n) {

    // Create a circular linked list of size N.
    struct Node* head = (struct Node*) malloc(sizeof(struct Node));
    head->data = 0;
    head->next = NULL;
    struct Node* prev = head;
    for (int i = 1; i < n; i++) {
        struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
        newNode->data = i;
        newNode->next = NULL;
        prev->next = newNode;
        prev = prev->next;
    }
    prev->next = head; // Connect last node to first

    // While only one node is left in the linked list
    struct Node* ptr1 = head;
    struct Node* ptr2 = head;
    while (ptr1->next != ptr1) {
        // Find m-th node
        int count = 1;
        while (count != m) {
            ptr2 = ptr1;
            ptr1 = ptr1->next;
            count += 1;
        }

        // Remove the m-th node
        ptr2->next = ptr1->next;
        free(ptr1);
        ptr1 = ptr2->next;
    }

    printf("The king will be %d\n", ptr1->data);
}

// Driver program to test the above function
int main() {
    int n, m;
    printf("Enter total number of monkeys in a group: ");
    scanf("%d", &n);
    printf("Enter m: ");
    scanf("%d", &m);
    monkeyKing(m, n);
    return 0;
}
