
typedef struct node
{
    int value;
    struct node *nextNode; // ¯\_(ツ)_/¯ tiene que ser asi

}str_Node, *ptr_Node;


ptr_Node newEmptyNode();
ptr_Node newNode(int value);