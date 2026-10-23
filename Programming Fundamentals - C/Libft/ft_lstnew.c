/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/27 20:38:04 by aal-moum          #+#    #+#             */
/*   Updated: 2025/12/27 20:40:31 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstnew(void *content)
{
	t_list	*st;

	st = (t_list *)malloc(sizeof(t_list));
	if (!st)
		return (NULL);
	st->content = content;
	st->next = NULL;
	return (st);
}
