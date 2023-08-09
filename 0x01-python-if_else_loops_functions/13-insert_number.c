#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: pointer to the head node
 * @number: the number to be added
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current = *head;
	listint_t *temp;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (!head || !*head || number <= current->n)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current)
	{
		if (current->next && current->next->n < number)
		{
			current = current->next;
		}
		else
		{
			temp = current->next;
			current->next = new_node;
			new_node->next = temp;
			break;
		}
	}
	return (new_node);
}
