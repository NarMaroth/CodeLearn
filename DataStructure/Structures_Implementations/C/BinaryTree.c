#include <stdio.h>
#include <stdlib.h>
#include "BinaryTree.h"

void insert(ptr_TreeNode* binary_tree, int value)
{

    if(*binary_tree == NULL) 
    {
        ptr_TreeNode tmp = (ptr_TreeNode)malloc(sizeof(str_TreeNode));
        tmp->leftChild = tmp->rightChild = NULL;
        tmp->data = value;
        *binary_tree = tmp;
        return;
    }

    // me muevo recursivamente hasta llegar al leaf que pertenece
    if(value < (*binary_tree)->data) 
    {
        insert(&(*binary_tree)->leftChild, value);
    } 
    else if(value > (*binary_tree)->data) 
    {
        insert(&(*binary_tree)->rightChild, value);
    }
}

ptr_TreeNode search(ptr_TreeNode* binary_tree, int value) {

    if(*binary_tree == NULL) 
    {
        return NULL;
    }

    // me muevo recursivamente hasta llegar al leaf con el value buscado o
    // devuelvo NULL
    if(value == (*binary_tree)->data) 
    {
        return (*binary_tree);
    } 
    else if(value < (*binary_tree)->data) 
    {
        search(&((*binary_tree)->leftChild), value);
    } 
    else if(value > (*binary_tree)->data)
    {
        search(&((*binary_tree)->rightChild), value);
    }
}

void delete_tree(ptr_TreeNode binary_tree) 
{
    if (binary_tree) 
    {
        delete_tree(binary_tree->leftChild);
        delete_tree(binary_tree->rightChild);
        free(binary_tree);
    }
}

void display_preorder(ptr_TreeNode binary_tree) 
{
    if (binary_tree) 
    {
        printf("%d\n",binary_tree->data);
        display_preorder(binary_tree->leftChild);
        display_preorder(binary_tree->rightChild);
    }
}

void display_inorder(ptr_TreeNode binary_tree) 
{
    if (binary_tree) 
    {
        display_inorder(binary_tree->leftChild);
        printf("%d\n",binary_tree->data);
        display_inorder(binary_tree->rightChild);
    }
}

void display_postorder(ptr_TreeNode binary_tree) 
{
    if (binary_tree) 
    {
        display_postorder(binary_tree->leftChild);
        display_postorder(binary_tree->rightChild);
        printf("%d\n",binary_tree->data);
    }
}
