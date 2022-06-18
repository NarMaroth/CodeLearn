#include "node.h"

typedef struct
{
    ptr_Node front;
    ptr_Node end;
}str_Queue,*ptr_Queue;

void create(ptr_Queue queue);

void enqueue(ptr_Queue queue, int value);

int dequeue(ptr_Queue queue);

bool isEmpty(ptr_Queue queue);