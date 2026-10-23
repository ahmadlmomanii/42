/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_duplicate.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 18:29:27 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 18:42:23 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	dup_check(t_node *a)
{
	t_node	*cur;
	t_node	*check;

	cur = a;
	while (cur)
	{
		check = cur->next;
		while (check)
		{
			if (check->data == cur->data)
				error_exit();
			check = check->next;
		}
		cur = cur->next;
	}
}
