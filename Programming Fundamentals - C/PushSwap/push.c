/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 18:29:27 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 18:42:23 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	push(t_node **st_from, t_node **st_to)
{
	t_node	*tmp;

	if (!st_from || !*st_from)
		return ;
	tmp = *st_from;
	*st_from = tmp->next;
	tmp->next = *st_to;
	*st_to = tmp;
}

void	pa(t_ps *ps)
{
	if (!ps->b)
		return ;
	push(&ps->b, &ps->a);
	ps->size_a++;
	ps->size_b--;
	if (ps->bench_on)
	{
		ps->bench.pa++;
		ps->bench.count++;
	}
	write(1, "pa\n", 3);
}

void	pb(t_ps *ps)
{
	if (!ps->a)
		return ;
	push(&ps->a, &ps->b);
	ps->size_a--;
	ps->size_b++;
	if (ps->bench_on)
	{
		ps->bench.pb++;
		ps->bench.count++;
	}
	write(1, "pb\n", 3);
}
