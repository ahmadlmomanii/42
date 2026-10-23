/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/11 18:38:48 by aal-moum          #+#    #+#             */
/*   Updated: 2025/12/27 23:21:00 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char		b;
	const unsigned char	*p;
	size_t				i;

	b = (unsigned char) c;
	p = (const unsigned char *)s;
	i = 0;
	while (i < n)
	{
		if (p[i] == b)
			return ((void *)(p + i));
		i++;
	}
	return (NULL);
}
