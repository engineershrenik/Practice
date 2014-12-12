#include <stdio.h>
#include <stdlib.h>



//Structure for linked List

typedef struct node{
	int inodeData;
	struct node *pNextNode;
}node_t;


//Insert Node at beginning of node
void pushBegin(node_t **pHead, int iData)
{
	node_t *new_node = (node_t *)malloc(sizeof(node_t));
	new_node->inodeData = iData;
	new_node->pNextNode =  *pHead;
	*pHead = new_node;	
}



//Insert node at the end
void pushEnd(node_t **pHeadRef, int iData)
{

	node_t *last = *pHeadRef;	
	node_t *new_node = (node_t *)malloc(sizeof(node_t));
	if (*pHeadRef == NULL)
	{
		*pHeadRef = new_node;	//from pHead->NULL to pHead->|new_node|pNextNode|->NULL
		new_node->pNextNode = NULL;
	}
	else
	{
		while(last->pNextNode != NULL)	//Iterate throught Linked List till you find Last node
		{	
			last = last->pNextNode;
		}
		
		last->pNextNode = new_node;
		
			
	}
	new_node->inodeData = iData;

	
}



//Insert node after N node
void addNodeAfterN(node_t *p_prevNode, int iData)
{
	if(p_prevNode == NULL)
	{
		printf("ERROR : Given node is NULL");
	}
	
	node_t *new_node  = (node_t *)malloc(sizeof(node_t));
	new_node->pNextNode = p_prevNode->pNextNode;
	new_node->inodeData = iData;
	p_prevNode->pNextNode = new_node;

	
}



//Show Linked List
void showLinkedList(node_t *pHead)
{
	while(pHead != NULL){
		printf("[%d]\t",pHead->inodeData);
		pHead = pHead->pNextNode;
	}
}




//Main program

int main()
{
	node_t *test = NULL;
//	pushBegin(&test, 100);
//	pushBegin(&test,34);
	pushEnd(&test, 77);
	pushEnd(&test, 54);
	addNodeAfterN(test->pNextNode,88);
	pushEnd(&test, 99);
	showLinkedList(test);
}
