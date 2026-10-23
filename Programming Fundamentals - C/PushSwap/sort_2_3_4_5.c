/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_2_3_4_5.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 14:51:00 by aal-moum          #+#    #+#             */
/*   Updated: 2026/03/26 20:09:24 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	five_helper(t_ps *ps, int m);

void	sort_two(t_ps *ps)
{
	if (ps->a->data > ps->a->next->data)
		sa(ps);
}

void	sort_five(t_ps *ps)
{
	int	m;

	m = find_min(ps);
	five_helper(ps, m);
	pb(ps);
	m = find_min(ps);
	five_helper(ps, m);
	pb(ps);
	sort_three(ps);
	pa(ps);
	pa(ps);
}

void	five_helper(t_ps *ps, int m)
{
	int	index;

	while (ps->a->data != m)
	{
		index = index_for_ps(ps->a, m);
		if (index > ps->size_a / 2)
			rra(ps);
		else
			ra(ps);
	}
}

void	sort_three(t_ps *ps)
{
	int	a;
	int	b;
	int	c;

	a = ps->a->data;
	b = ps->a->next->data;
	c = ps->a->next->next->data;
	if (a < b && b < c)
		return ;
	else if (a > b && a < c)
		sa(ps);
	else if (a > b && b > c)
	{
		sa(ps);
		rra(ps);
	}
	else if (a > b && a > c && b < c)
		ra(ps);
	else if (a < b && b > c && a < c)
	{
		sa(ps);
		ra(ps);
	}
	else if (a < b && b > c && a > c)
		rra(ps);
}

void	sort_four(t_ps *ps)
{
	int	m;

	m = find_min(ps);
	five_helper(ps, m);
	pb(ps);
	sort_three(ps);
	pa(ps);
}
