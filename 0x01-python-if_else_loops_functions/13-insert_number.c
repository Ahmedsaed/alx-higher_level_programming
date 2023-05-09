#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: pointer to the first node of the inked list
 * @number: the number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	if (head == NULL)
		return (NULL);
	current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current != NULL && current->next != NULL)
	{
		if (current->next->n >= number)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}

		current = current->next;
	}

	new_node->next = NULL;
	current->next = new_node;
	return (new_node);
}
