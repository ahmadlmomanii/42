/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   build_stack_a.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 16:21:08 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	push_to_stack(char *av, t_ps *ps)
{
	int		value;
	t_node	*b;

	value = ft_atoi_strict(av);
	b = new_node(value);
	node_add_back(&ps->a, b);
	ps->size_a++;
}

void	build_stack_a(int i, char **av, t_ps *ps, int ac)
{
	char	**parts;
	int		k;

	while (i < ac)
	{
		k = 0;
		if (has_space(av[i]))
		{
			parts = ft_split(av[i]);
			if (!parts[0])
			{
				ft_free_split(parts);
				error_exit();
			}
			while (parts[k])
			{
				push_to_stack(parts[k], ps);
				k++;
			}
			ft_free_split(parts);
		}
		else
			push_to_stack(av[i], ps);
		i++;
	}
}
