/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_helper.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 16:21:08 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	ft_sqrt(int n)
{
	int	i;

	if (n <= 0)
		return (0);
	i = 1;
	while (i <= n / i)
		i++;
	return (i - 1);
}

int	find_index(int *arr, int size, int data)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (arr[i] == data)
			return (i);
		i++;
	}
	return (-1);
}

int	find_max(t_node *stack)
{
	int		max;
	t_node	*cur;

	if (!stack)
		return (0);
	max = stack->data;
	cur = stack->next;
	while (cur)
	{
		if (cur->data > max)
			max = cur->data;
		cur = cur->next;
	}
	return (max);
}

int	position(t_node *stack, int value)
{
	int		pos;
	t_node	*cur;

	pos = 0;
	cur = stack;
	while (cur)
	{
		if (cur->data == value)
			return (pos);
		pos++;
		cur = cur->next;
	}
	return (-1);
}
