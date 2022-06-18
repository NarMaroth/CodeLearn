#include <stdlib.h> 
#include <stdbool.h>
#include "PriorityQueue.h"


void create(ptr_PriorityQueue queue)
{
    queue->end = NULL;
    queue->front = NULL;
}

void enqueue(ptr_PriorityQueue queue, int value,bool ascending)
{
    ptr_Node node = newNode(value);

    if(isEmpty(queue))
    {
        queue->front = node;
        queue->end = node;
    }
    else
    {
        ptr_Node prevNode = NULL;
        ptr_Node currentNode = queue->front;
        ptr_Node nextNode = currentNode->nextNode;

        if(ascending)
        {
            while (currentNode != NULL && currentNode->value < node->value)
            {
                prevNode = currentNode;
                currentNode = currentNode->nextNode;
                nextNode = currentNode->nextNode;
            }
        }
        else
        {
            while (currentNode != NULL && currentNode->value > node->value)
            {
                prevNode = currentNode;
                currentNode = currentNode->nextNode;
                nextNode = currentNode->nextNode;
            }
        }

        if(currentNode == NULL) // llegue al final de la fila
        {
            prevNode->nextNode = node;
            queue->end = node;
        }
        else if(prevNode == NULL) // si se debe remplazar el primer nodo
        {
            queue->front = node;
            node->nextNode = currentNode;
        }
        else
        {
            currentNode->nextNode = node;
            node->nextNode = nextNode;
        }
    }
    
    return;
}

int dequeue(ptr_PriorityQueue queue)
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

bool isEmpty(ptr_PriorityQueue queue)
{
    return queue->front == NULL && queue->end == NULL;
}