#include "lists.h"

/**
 * check_cycle - checks if a list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *last = list;

	while (first != NULL && first->next != NULL)
	{
		last = last->next;
		first = first->next->next;
		if (last == first)
			return (1);
	}
	return (0);
}
