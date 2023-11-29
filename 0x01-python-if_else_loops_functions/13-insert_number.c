#include "lists.h"

/**
 * insert_node - inserts a  number into a sorted singly linked list
 * @head: the beginning of the list
 * @number: the number to add
 * Return: address of new node or Null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new, *pre;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (node != NULL && node->n < number)
	{
		pre = node;
		node = node->next;
	}

	if (pre == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		pre->next = new;
		new->next = node;
	}

	return (new);
}
