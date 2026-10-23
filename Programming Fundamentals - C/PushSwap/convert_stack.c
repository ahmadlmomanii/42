/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   complex_sort.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 16:21:08 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	convert_stack(t_ps *ps)
{
	int		*arr;
	t_node	*current;
	int		i;
	int		size;

	size = ps->size_a;
	arr = malloc(sizeof(int) * size);
	if (!arr)
		error_exit();
	current = ps->a;
	i = 0;
	while (current)
	{
		arr[i] = current->data;
		i++;
		current = current->next;
	}
	sort_array(arr, size);
	current = ps->a;
	while (current)
	{
		current->data = find_index(arr, size, current->data);
		current = current->next;
	}
	free(arr);
}
