#include "lists.h"

/**
 * is_palindrome - checks  if a singly linked list is a palindrome
 *
 * @head: pointer to the head of the node
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *turtle = *head, *hare = *head;
	listint_t *prev = NULL, *current = NULL, *nxt = NULL;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	while (hare->next && hare->next->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (hare == turtle)
			return (0);
	}

	current = turtle->next;

	while (current)
	{
		nxt = current->next;
		current->next = prev;
		prev = current;
		current = nxt;
	}

	nxt = *head;

	while (nxt != NULL && prev != NULL)
	{
		if (nxt->n != prev->n)
			return (0);
		nxt = nxt->next;
		prev = prev->next;
	}
	return (1);
}
