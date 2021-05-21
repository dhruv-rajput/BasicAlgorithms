#include <stdio.h>
#include <stdlib.h>
struct Node
{
  int data;
  struct Node *next;
};

struct Node* head;

void push(int new_data)
{
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
  
    new_node->data  = new_data;
  
    new_node->next = head;
    head    = new_node;
}

void printList()
{
  while (head != NULL)
  {
     printf(" %d ", head->data);
     head = head->next;
  }
}
  

int main()
{
  head = NULL;
  
  
  push(7);
  
  push(1);
  
  printf("\n Created Linked list is: ");
  printList();
  
  return 0;
}