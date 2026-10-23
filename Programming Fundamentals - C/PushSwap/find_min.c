/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   find_min.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/03/26 22:37:09 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	find_min(t_ps *ps)
{
	t_node	*cur;
	int		min;

	cur = ps->a;
	min = ps->a->data;
	while (cur)
	{
		if (min > cur->data)
			min = cur->data;
		cur = cur->next;
	}
	return (min);
}
