/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 18:29:27 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 18:42:23 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

t_node	*new_node(int value)
{
	t_node	*node;

	node = malloc(sizeof(t_node));
	if (!node)
		error_exit();
	node->data = value;
	node->next = NULL;
	return (node);
}

void	node_add_back(t_node **a, t_node *new)
{
	t_node	*last;

	if (*a == NULL)
	{
		*a = new;
		return ;
	}
	last = *a;
	while (last->next != NULL)
		last = last->next;
	last->next = new;
}

void	stack_free(t_node **a)
{
	t_node	*next;
	t_node	*cur;

	cur = *a;
	while (cur)
	{
		next = cur->next;
		free(cur);
		cur = next;
	}
	*a = NULL;
}
