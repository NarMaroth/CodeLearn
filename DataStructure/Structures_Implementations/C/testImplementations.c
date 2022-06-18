#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "BinaryTree.h"

int main()
{
    
    ptr_TreeNode root_node = (ptr_TreeNode)malloc(sizeof(str_TreeNode));
    insert(&root_node, 10);
    insert(&root_node, 30);
    insert(&root_node, 25);
    insert(&root_node, 36);
    insert(&root_node, 56);
    insert(&root_node, 78);
    display_preorder(root_node);
    return 0;
}