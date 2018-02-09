#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 80 /* 80 chars per line, per command, should be enough. */

typedef struct node
{
	char		 data[ MAX_LINE ];
	struct node* prevPtr;
	struct node* nextPtr;
} Node;

typedef struct linkedList
{
	Node* header;
	Node* tail;
} LinkedList;

// Find out how many nodes there are in the given linked list.
int GetLinkedListSize( const LinkedList* ll )
{
    int size = 0;
    Node* tempNode = ll->header;
    while( tempNode != ll->tail )
    {
        tempNode = tempNode->nextPtr;
        size++;
    }

    return size;
}

// Insert new data at the end of LL.
void InsertIntoLinkedList( LinkedList* ll, const char* newData )
{
	Node* newNode = NULL;

	// Create new node and assign values to its fields.
	newNode = ( Node* )malloc( sizeof( Node ) );
	strcpy( newNode->data, newData );
	newNode->nextPtr = NULL;
	newNode->prevPtr = NULL;

	if( ll->header == NULL ) // If LL is empty, newNode will be the first & last node for now.
	{
		ll->header = newNode;
		ll->tail   = newNode;
	}
	else
	{
		// Insert the new node at the end of LL.
		newNode->prevPtr  = ll->tail; // newNode's prevPtr points to current last node.
		ll->tail->nextPtr = newNode;  // Currently last node's nextPtr now points to newNode.
		ll->tail		  = newNode;  // New tail is the newNode.
	}
}

// Finds the node located "pos" number of nodes away from the beginning of the given linked list.
void LocateNode( const LinkedList* ll, Node** ptrToNode, int pos )
{
	*ptrToNode = ll->header;

	while( pos-- != 0 )
		*ptrToNode = ( *ptrToNode )->nextPtr;
}

// Finds the node located "pos" number of nodes away from the end of the given linked list.
void ReverseLocateNode( const LinkedList* ll, Node** ptrToNode, int pos )
{
	*ptrToNode = ll->tail;

	while( pos-- != 0 )
		*ptrToNode = ( *ptrToNode )->prevPtr;
}

// Returns the data of the node located "pos" number of nodes away from the beginning of the given linked list.
char* LocateData( const LinkedList* ll, const int pos )
{
	Node* tempNodePtr;
	LocateNode( ll, &tempNodePtr, pos );
	return tempNodePtr->data;
}

// Returns the data of the node located "pos" number of nodes away from the end of the given linked list.
char* ReverseLocateData( const LinkedList* ll, const int pos )
{
	Node* tempNodePtr;
	ReverseLocateNode( ll, &tempNodePtr, pos );
	return tempNodePtr->data;
}

// Removes the element at the given position from the given linked list.
void RemoveFromLinkedList( LinkedList* ll, const int pos )
{
	Node* nodeToBeRemovedPtr;

	// Find the node to be deleted.
	LocateNode( ll, &nodeToBeRemovedPtr, pos );

	// Check if the node to be removed is the header node.
	if( nodeToBeRemovedPtr == ll->header )
	{
		ll->header = ll->header->nextPtr;
	}
	// Check if the node to be removed is the tail node.
	if( nodeToBeRemovedPtr == ll->tail )
	{
		ll->tail = ll->tail->prevPtr;
	}

	// Point prevPtr to nextPtr and nextPtr to prevPtr respectively.
	if( nodeToBeRemovedPtr->prevPtr != NULL )
	{
		nodeToBeRemovedPtr->prevPtr->nextPtr = nodeToBeRemovedPtr->nextPtr;
	}
	if( nodeToBeRemovedPtr->nextPtr != NULL )
	{
		nodeToBeRemovedPtr->nextPtr->prevPtr = nodeToBeRemovedPtr->prevPtr;
	}

	// Nobody points to this node anymore, safe to delete.
	free( nodeToBeRemovedPtr );
}

// Prints the given linked list.
void PrintLinkedList( const LinkedList* ll, int withIndex )
{
	Node* llPtr = ll->header;
	int	  i;

	for( i = 0; llPtr != NULL; i++ )
	{
		if( withIndex )
		{
			printf( "%d ", i );
		}
		printf( "%s\n", llPtr->data );
		llPtr = llPtr->nextPtr;
	}
}

// Deallocates every node in a given linked list.
void Deallocate( LinkedList* ll )
{
	Node* tempNodePtr;
	Node* llPtr = ll->header;
	int	  i;

	for( i = 0; llPtr != NULL; i++ )
	{
		tempNodePtr = llPtr;
		llPtr		= llPtr->nextPtr;
		free( tempNodePtr );
	}

	ll->header = NULL;
	ll->tail   = NULL;
}
