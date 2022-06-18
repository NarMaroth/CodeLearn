#include "node.h"

ptr_Node insertInFront(ptr_Node* list, ptr_Node value);

ptr_Node insertAtEnd(ptr_Node* list, ptr_Node value);

ptr_Node insertOrdered(ptr_Node* lista, int value);

ptr_Node search(ptr_Node lista, int value);

int deleteFirst(ptr_Node* lista);

int delete(ptr_Node* lista, int value);

void clearList(ptr_Node* lista);

void sortList(ptr_Node* lista);

ptr_Node inserwithoutDuplicates(ptr_Node* lista, int value);

void printList(ptr_Node lista);

ptr_Node insertAt(ptr_Node* lista, int value, int pos);