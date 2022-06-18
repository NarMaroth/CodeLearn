#include <stdlib.h> 
#include <stdbool.h>
#include "Queue.h"


void create(ptr_Queue queue)
{
    queue->end = NULL;
    queue->front = NULL;
}

void enqueue(ptr_Queue queue, int value)
{
    // Creacion nuevo nodo
    ptr_Node nodo = newNode(value);

    // Insertamos el nuevo nodo en la cola
    if(queue->front == NULL)
    {
        queue->front = nodo;
    }
    else
    {
        // seteo al nodo actual que se encuentre en front, a que apunte al nuevo nodo
        queue->end->nextNode = nodo;
    }
    
    queue->end = nodo;
    
    return;
}

int dequeue(ptr_Queue queue)
{
    int valor = queue->front->value;

    ptr_Node aux = queue->front;
    queue->front = queue->front->nextNode;

    if(queue->front == NULL)
    {
        queue->end = NULL;
    }

    free(aux);

    return valor;
}

bool isEmpty(ptr_Queue queue)
{
    return queue->front == NULL && queue->end == NULL;
}