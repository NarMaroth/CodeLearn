#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "list.h"


int main()
{
    // generar list
    ptr_Node list = NULL;

    return 0;
}


ptr_Node insertInFront(ptr_Node* list, ptr_Node value)
{
    ptr_Node node = newNode(value);

    node->nextNode = *list;
    *list = node;

    return node;
}

ptr_Node insertAtEnd(ptr_Node* list, ptr_Node value)
{
    ptr_Node node = newNode(value);

    // si la list esta vacia
    if(*list == NULL)
    {
        *list = node;
    }
    else
    {
        // avanzar hasta encontrar el ultimo node en la list
        ptr_Node listaAux = *list;
        while (listaAux != NULL && listaAux->nextNode != NULL)
        {
            listaAux = listaAux->nextNode;
        }

        listaAux->nextNode = node;
    }

    return node;
}

ptr_Node insertOrdered(ptr_Node* list, int value)
{
    ptr_Node node = newNode(value);

    ptr_Node listaAux = *list;
    ptr_Node nodoPrev = NULL;

    if(listaAux == NULL)
    {
        *list = node;
    }
    else
    {
        // avanzar hasta encontrar el node con value mayor al creado
        while (listaAux != NULL && value < listaAux->value)
        {
            nodoPrev = listaAux;
            listaAux = listaAux->nextNode;
        }

        // si es menor al primer node, se pone al inicio y se setea el antigup
        //primer node como el nextNode a este.
        if(nodoPrev == NULL)
        {
            node->nextNode = listaAux;
            listaAux = node;
        }
        else
        {
            nodoPrev->nextNode = node;
            node->nextNode = listaAux;
        }
    }
    
    return node;
    
}


ptr_Node search(ptr_Node list, int value)
{
    ptr_Node listaAux = list;

    while (listaAux != NULL && listaAux->value != value){}
    {
        listaAux = listaAux->nextNode;
    }

    return  listaAux;
}

int deleteFirst(ptr_Node* list)
{
    int value = (*list)->value;

    ptr_Node nodoAux = *list;
    *list = (*list)->nextNode;

    free(nodoAux);

    return value;
}

int delete(ptr_Node* list, int value)
{
    ptr_Node auxList = *list;
    ptr_Node prevNode = NULL;

    while (auxList != NULL && auxList->value != value)
    {
        prevNode = auxList;
        auxList = auxList->nextNode;
    }

    // si es el primer node de la list
    if(prevNode == NULL)
    {
        *list = (*list)->nextNode; //list pasa a null
    }
    else
    {
        prevNode->nextNode = auxList->nextNode; 
    }

    int value = auxList->value;
    free(auxList);
    return value;
}

void clearList(ptr_Node* list)
{
    ptr_Node auxNode;
    while (*list != NULL)
    {
        auxNode = *list;
        *list = (*list)->nextNode;
        free(auxNode);
    }

    return;
}

void sortList(ptr_Node* list)
{
    int value;
    ptr_Node newList;

    while (list != NULL)
    {
        value = deleteFirst(list);
        insertOrdered(&newList, value);
    }

    *list = newList;
    return;
}

ptr_Node inserwithoutDuplicates(ptr_Node* list, int value)
{
    ptr_Node node = search(*list,value);

    if(node != NULL)
    {
        node = insertOrdered(list,value);
    }

    return node;
}

void printList(ptr_Node list)
{
    while (list != NULL)
    {
        printf("Dato: %d",list->value);
        list = list->nextNode;
    }

    // list es una copia de la verdadera list por lo que da igual que se
    //modifique   
    return;
}

ptr_Node insertAt(ptr_Node* list, int value, int pos)
{
    ptr_Node node = newNode(value);

    ptr_Node auxNode = *list;
    ptr_Node prevNode = NULL;

    for (size_t i = 0; i<pos && auxNode != NULL ; i++)
    {
        prevNode = auxNode;
        auxNode = auxNode->nextNode;
    }

    if(prevNode == NULL) // si la pos esta fuera de rango
    {
        *list = node; // se añade al final
    }
    else
    {
        prevNode->nextNode = node;
    }

    node->nextNode = auxNode;
    return node;
}