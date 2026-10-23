/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   complex_sort.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/03/26 22:37:09 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	sort_complex(t_ps *ps)
{
	int	size;
	int	max_bits;

	if (ps->size_a <= 5)
	{
		small_selector(ps);
		return ;
	}
	convert_stack(ps);
	size = ps->size_a;
	max_bits = get_max_bits(size - 1);
	complex_helper(max_bits, ps, size);
}

void	complex_helper(int max_bits, t_ps *ps, int size)
{
	int	i;
	int	j;

	i = 0;
	while (i < max_bits)
	{
		j = 0;
		while (j < size)
		{
			if (((ps->a->data >> i) & 1) == 0)
				pb(ps);
			else
				ra(ps);
			j++;
		}
		while (ps->b)
			pa(ps);
		i++;
	}
}

int	get_max_bits(int max)
{
	int	bits;

	bits = 0;
	while ((max >> bits) != 0)
		bits++;
	return (bits);
}
