#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head
 * @number: an integer
 * Return: a pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ncurrent, *point;

	ncurrent = *head;
	point = malloc(sizeof(listint_t));
	point->n = number;
	if (point == NULL)
		return (NULL);
	if (ncurrent == NULL || ncurrent->n >= number)
	{
		point->next = ncurrent;
		*head = point;
		return (point);
	}
	while (ncurrent && ncurrent->next && ncurrent->next->n < number)
		ncurrent = ncurrent->next;
	point->next = ncurrent->next;
	ncurrent->next = point;
	return (point);
}
