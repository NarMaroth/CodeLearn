#include <stdlib.h>
#include "node.h"

ptr_Node newEmptyNode()
{
    ptr_Node node = (ptr_Node)malloc(sizeof(str_Node));
    
    node->value = (int)NULL;
    node->nextNode = NULL;

    return node;
}

ptr_Node newNode(int value)
{
    ptr_Node node = (ptr_Node)malloc(sizeof(str_Node));

    node->value = value;
    node->nextNode = NULL;

    return node;
}