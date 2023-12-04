#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is palindrome.
 * @head: pointer to pointer to head node.
 * Return: 1 if palindrome otherwise 0.
 */
int is_palindrome(listint_t **head)
{
	int *list, i, j;
	listint_t *len;

	list = malloc(sizeof(int));
	if (list == NULL)
		exit(EXIT_FAILURE);

	len = *head;
	i = 1;

	while (len)
	{
		list[i++ - 1] = len->n;
		list = realloc(list, sizeof(int) * i);
		len = len->next;
	}

	i -= 1;
	j = 0;

	while (j <= i/2)
	{
		if (list[j] != list[i - j - 1])
			return (0);

		j++;
	}

	return (1);
}
