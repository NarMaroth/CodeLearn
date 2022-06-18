#include "node.h"

typedef struct treeNode
{
    int data;
    struct treeNode* leftChild;
    struct treeNode* rightChild;
}str_TreeNode,*ptr_TreeNode;

void insert(ptr_TreeNode* binary_tree, int value);

ptr_TreeNode search(ptr_TreeNode* binary_tree, int value);

void delete_tree(ptr_TreeNode binary_tree);

//It displays in order. First root node, then left node and then right node.
void display_preorder(ptr_TreeNode binary_tree);

//It displays first left node, then root node and then right node.
void display_inorder(ptr_TreeNode binary_tree);

//It displays first left node, then right node and then root node.
void display_postorder(ptr_TreeNode binary_tree);