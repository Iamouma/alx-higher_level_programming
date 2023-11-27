#include "lists.h"
/**
 * check_cycle - checks if a singly linked lt has a cycle.
 * @list: item number one in the list.
 * Return: 0 Success, 1 Fail
 */
int check_cycle(listint_t *list)
{
	listint_t *len = list;
	listint_t *count = list;

	if (!list)
		return (0);

	while (len &&count && count->next)
	{
		len = len->next;
		count = count->next->next;

		if (len == count)
			return (1);
	}

	return (0);
}
