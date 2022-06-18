#include <stdlib.h> 
#include <stdbool.h>
#include "node.h"

bool isEmpty(ptr_Node head);
void push(ptr_Node *head, int value);
int pop(ptr_Node *head);
void clear(ptr_Node *head);

int main()
{
    ptr_Node head = NULL; // crear stack
    return 0;
}

bool isEmpty(ptr_Node head)
{
    return head == NULL;
}

void push(ptr_Node *head, int value)
{
    // Creacion del nodo
    ptr_Node nodo = (ptr_Node) malloc(sizeof(str_Node));

    nodo->value = value;

    // añado el contenido de head como nextNode puntero del nodo
    nodo->nextNode = *head;
    // seteo contenido de head como el nodo recien creado
    *head = nodo->nextNode;

    return;
}

int pop(ptr_Node *head)
{
    // guarda valor a retornar
    int valor = (*head)->value;

    // guardo dir. de nodo actual al que apunta head para eliminarlo mas tarde
    ptr_Node nodoAux = *head;

    // hago que head sea la pos de memoria del nextNode nodo
    *head = (*head)->nextNode;

    // borro de memoria el nodo que anterior mente era head
    free(nodoAux);

    return valor;
}

void clear(ptr_Node *head)
{
    while (isEmpty(*head) == false)
    {
        pop(head);
    }
    
    *head = NULL;
    return;
}