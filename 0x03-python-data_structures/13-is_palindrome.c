#include "lists.h"
#include <stdio.h>
/**
 * reverse_listint - reverses a linked list
 * @head: a pointer
 * Return: void
 */

void reverse_listint(listint_t **head)
{
	listint_t *prece = NULL;
	listint_t *ncurrent = *head;
	listint_t *suiv = NULL;

	while (current)
	{
		suiv = ncurrent->next;
		ncurrent->next = prev;
		prece = ncurrent;
		ncurrent = suiv;
	}

	*head = prece;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *l = *head, *f = *head, *t = *head, *d = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			d = l->next;
			break;
		}
		if (!f->next)
		{
			d = l->next->next;
			break;
		}
		l = l->next;
	}

	reverse_listint(&d);

	while (d && t)
	{
		if (t->n == d->n)
		{
			d = d->next;
			t = t->next;
		}
		else
			return (0);
	}

	if (!d)
		return (1);

	return (0);
}
