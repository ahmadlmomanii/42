/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   disorder.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 14:51:00 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 18:12:35 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

double	compute_disorder(t_node *a, int size)
{
	t_node	*i_node;
	t_node	*j_node;
	long	mistakes;
	long	total_pairs;

	if (size <= 1)
		return (0.0);
	mistakes = 0;
	total_pairs = 0;
	i_node = a;
	while (i_node)
	{
		j_node = i_node->next;
		while (j_node)
		{
			total_pairs++;
			if (i_node->data > j_node->data)
				mistakes++;
			j_node = j_node->next;
		}
		i_node = i_node->next;
	}
	return ((double)mistakes / total_pairs);
}
