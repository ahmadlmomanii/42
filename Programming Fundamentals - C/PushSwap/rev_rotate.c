/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rev_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 18:29:27 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 18:42:23 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	rev_rotate(t_node **stack)
{
	t_node	*last;
	t_node	*prev;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	prev = NULL;
	last = *stack;
	while (last->next)
	{
		prev = last;
		last = last->next;
	}
	prev->next = NULL;
	last->next = *stack;
	*stack = last;
}

void	rra(t_ps *ps)
{
	if (!ps->a || !ps->a->next)
		return ;
	rev_rotate(&ps->a);
	if (ps->bench_on)
	{
		ps->bench.rra++;
		ps->bench.count++;
	}
	write(1, "rra\n", 4);
}

void	rrb(t_ps *ps)
{
	if (!ps->b || !ps->b->next)
		return ;
	rev_rotate(&ps->b);
	if (ps->bench_on)
	{
		ps->bench.rrb++;
		ps->bench.count++;
	}
	write(1, "rrb\n", 4);
}

void	rrr(t_ps *ps)
{
	if (!ps->a || !ps->a->next || !ps->b || !ps->b->next)
		return ;
	rev_rotate(&ps->a);
	rev_rotate(&ps->b);
	if (ps->bench_on)
	{
		ps->bench.rrr++;
		ps->bench.count++;
	}
	write(1, "rrr\n", 4);
}
