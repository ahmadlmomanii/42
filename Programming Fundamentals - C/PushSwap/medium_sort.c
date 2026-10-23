/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 16:21:08 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	sort_medium(t_ps *ps)
{
	int	chunks;

	chunks = ft_sqrt(ps->size_a);
	if (ps->size_a <= 5)
	{
		small_selector(ps);
		return ;
	}
	convert_stack(ps);
	push_and_rotate_a(chunks, ps);
}

void	push_and_rotate_a(int chunks, t_ps *ps)
{
	int	i;

	i = 0;
	while (ps->a)
	{
		if (ps->a->data <= i)
		{
			pb(ps);
			rb(ps);
			i++;
		}
		else if (ps->a->data <= i + chunks)
		{
			pb(ps);
			i++;
		}
		else
			ra(ps);
	}
	push_and_rotate_b(ps);
}

void	push_and_rotate_b(t_ps *ps)
{
	int	max;
	int	pos;

	while (ps->b)
	{
		max = find_max(ps->b);
		while (ps->b->data != max)
		{
			pos = position(ps->b, max);
			if (pos <= ps->size_b / 2)
				rb(ps);
			else
				rrb(ps);
		}
		pa(ps);
	}
}

void	sort_array(int *arr, int size)
{
	int	i;
	int	j;
	int	min;
	int	tmp;

	i = 0;
	while (i < size - 1)
	{
		min = i;
		j = i + 1;
		while (j < size)
		{
			if (arr[j] < arr[min])
				min = j;
			j++;
		}
		tmp = arr[i];
		arr[i] = arr[min];
		arr[min] = tmp;
		i++;
	}
}
