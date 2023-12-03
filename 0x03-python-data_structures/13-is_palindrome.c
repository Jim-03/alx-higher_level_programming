#include "lists.h"

/**
 * is_palindrome - checks if the list is a palindrome
 * @head: the start of the list
 * Return: 0 if not, 1 if yes
 */

int is_palindrome(listint_t **head)
{
	int length = 0, i, idx;
	listint_t *temp, *current;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		length++;
		current = current->next;
	}
	current = *head;
	for (i = 0; i < length; i++)
	{
		temp = *head;
		idx = 0;
		while (temp && idx < length - i)
		{
			temp = temp->next;
			idx++;
		}
		if (temp->n != current->n)
			return (0);
		current = current->next;
	}
	return (1);
}
