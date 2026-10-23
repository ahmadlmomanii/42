/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simple_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 14:51:00 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 18:12:35 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	ra_or_rra(t_ps *ps, int min)
{
	int		size;
	t_node	*cur;
	int		min_index;

	size = ps->size_a;
	cur = ps->a;
	min_index = 0;
	while (cur)
	{
		if (cur->data == min)
			break ;
		min_index++;
		cur = cur->next;
	}
	return ((size / 2) >= min_index);
}

void	sort_simple(t_ps *ps)
{
	int	min;
	int	i;

	if (ps->size_a <= 5)
	{
		small_selector(ps);
		return ;
	}
	while (ps->size_a > 3)
	{
		min = find_min(ps);
		i = ra_or_rra(ps, min);
		while (ps->a->data != min)
		{
			if (i)
				ra(ps);
			else
				rra(ps);
		}
		pb(ps);
	}
	sort_three(ps);
	while (ps->size_b > 0)
		pa(ps);
}
