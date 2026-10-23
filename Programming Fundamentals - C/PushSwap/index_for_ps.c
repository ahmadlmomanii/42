/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   index_for_ps.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 14:51:00 by aal-moum          #+#    #+#             */
/*   Updated: 2026/03/26 20:09:24 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	index_for_ps(t_node *a, int data)
{
	int	i;

	i = 0;
	while (a)
	{
		if (a->data == data)
			return (i);
		a = a->next;
		i++;
	}
	return (-1);
}
