#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a structure
 * Return: integer.
 */

int check_cycle(listint_t *list)
{
	listint_t *lent, *f;

	lent = list;
	f = list;
	if (list == NULL)
	{
		return (0);
	}
	f = f->next;
	while (f && f->next && lent != NULL)
	{
		if (lent == f)
		{
			return (1);
		}
		lent= lent->next;
		f = f->next->next;
	}
	return (0);
}
