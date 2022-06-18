#include "node.h"

typedef struct
{
    ptr_Node front;
    ptr_Node end;
}str_PriorityQueue,*ptr_PriorityQueue;

void create(ptr_PriorityQueue queue);

void enqueue(ptr_PriorityQueue queue, int value, bool ascending);

int dequeue(ptr_PriorityQueue queue);

bool isEmpty(ptr_PriorityQueue queue);