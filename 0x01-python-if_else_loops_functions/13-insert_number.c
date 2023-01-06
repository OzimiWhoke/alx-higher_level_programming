#include "lists.h"



/**
 *
 * * insert_node - a function that inserts a number into a sorted linked list
 *
 * * @head: the head of the linked list
 *
 * * @number: the number to be inserted
 *
 * * Return: returns the address of the new node or NULL if failed
 *
 * */

listint_t *insert_node(listint_t **head, int number)

{

		listint_t *tmp = *head;

			listint_t *new;



				new = malloc(sizeof(listint_t));

					if (!new)

								return (NULL);

						new->n = number;

							new->next = NULL;



								if (*head == NULL)

										{

													*head = new;

															return (new);

																}

									if ((tmp->n) >= number)

											{

														new->next = tmp;

																*head = new;

																		return (new);

																			}



										while (tmp)

												{

															if (!(tmp->next))

																		{

																						if ((tmp->n) <= number)

																										{

																															tmp->next = new;

																																			return (new);

																																						}

																								}

																	if ((tmp->next->n) >= number)

																				{

																								new->next = tmp->next;

																											tmp->next = new;

																														break;

																																}

																			tmp = tmp->next;

																				}

											return (new);

}
