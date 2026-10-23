/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   select_strategy.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 14:51:00 by aal-moum          #+#    #+#             */
/*   Updated: 2026/03/29 22:48:39 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	select_strategy(t_ps *ps)
{
	if (ps->flag == 0)
	{
		if (ps->bench.disorder < 0.2)
			ps->flag = 1;
		else if (ps->bench.disorder < 0.5)
			ps->flag = 2;
		else
			ps->flag = 3;
	}
}

void	execute_sort(t_ps *ps)
{
	if (ps->size_a <= 10)
		sort_simple(ps);
	else if (ps->flag == 1)
		sort_simple(ps);
	else if (ps->flag == 2)
		sort_medium(ps);
	else if (ps->flag == 3)
		sort_complex(ps);
}
