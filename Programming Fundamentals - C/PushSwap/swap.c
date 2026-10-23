/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 18:29:27 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 18:42:23 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	swap(t_node **stack)
{
	t_node	*first;
	t_node	*second;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	first = *stack;
	second = first->next;
	first->next = second->next;
	second->next = first;
	*stack = second;
}

void	sa(t_ps *ps)
{
	if (!ps->a || !ps->a->next)
		return ;
	swap(&ps->a);
	if (ps->bench_on)
	{
		ps->bench.sa++;
		ps->bench.count++;
	}
	write(1, "sa\n", 3);
}

void	sb(t_ps *ps)
{
	if (!ps->b || !ps->b->next)
		return ;
	swap(&ps->b);
	if (ps->bench_on)
	{
		ps->bench.sb++;
		ps->bench.count++;
	}
	write(1, "sb\n", 3);
}

void	ss(t_ps *ps)
{
	if (!ps->a || !ps->a->next || !ps->b || !ps->b->next)
		return ;
	swap(&ps->a);
	swap(&ps->b);
	if (ps->bench_on)
	{
		ps->bench.ss++;
		ps->bench.count++;
	}
	write(1, "ss\n", 3);
}
