/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 16:21:08 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	rotate(t_node **stack)
{
	t_node	*last;
	t_node	*first;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	last = *stack;
	first = *stack;
	while (last->next)
		last = last->next;
	*stack = first->next;
	first->next = NULL;
	last->next = first;
}

void	ra(t_ps *ps)
{
	if (!ps->a || !ps->a->next)
		return ;
	rotate(&ps->a);
	if (ps->bench_on)
	{
		ps->bench.ra++;
		ps->bench.count++;
	}
	write(1, "ra\n", 3);
}

void	rb(t_ps *ps)
{
	if (!ps->b || !ps->b->next)
		return ;
	rotate(&ps->b);
	if (ps->bench_on)
	{
		ps->bench.rb++;
		ps->bench.count++;
	}
	write(1, "rb\n", 3);
}

void	rr(t_ps *ps)
{
	if (!ps->a || !ps->a->next || !ps->b || !ps->b->next)
		return ;
	rotate(&ps->a);
	rotate(&ps->b);
	if (ps->bench_on)
	{
		ps->bench.rr++;
		ps->bench.count++;
	}
	write(1, "rr\n", 3);
}
