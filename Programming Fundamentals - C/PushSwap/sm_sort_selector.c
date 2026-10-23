/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sm_sort_selector.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 16:21:08 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	small_selector(t_ps *ps)
{
	if (ps->size_a == 5)
		sort_five(ps);
	else if (ps->size_a == 4)
		sort_four(ps);
	else if (ps->size_a == 3)
		sort_three(ps);
	else if (ps->size_a == 2)
		sort_two(ps);
}
