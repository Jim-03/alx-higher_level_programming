#include "lists.h"

/**
 * is_palindrome - checks if the list is a palindrome
 * @head: the start of the list
 * Return: 0 if not, 1 if yes
 */

int is_palindrome(listint_t **head)
{
	int length = 0, i, idx;
	listint_t *temp;

	if (head == NULL)
		return (1);
	while (*head)
		length++;
	for (i = 0; i < length; i++)
	{
		temp = *head;
		idx = 0;
		while ((head) && (idx < length))
		{
			temp = temp->next;
			length--;
		}
		if (temp->n != (*head)->n)
			return (0);
		*head = (*head)->next;
	}
	return (1);
}
