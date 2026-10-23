/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/27 20:08:33 by aal-moum          #+#    #+#             */
/*   Updated: 2025/12/27 23:07:02 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	len(int n)
{
	int	i;

	if (n == 0)
		return (1);
	i = 0;
	while (n != 0)
	{
		i++;
		n /= 10;
	}
	return (i);
}

char	*ft_itoa(int n)
{
	int			i;
	char		*c;
	long int	nb;

	i = len(n);
	nb = n;
	if (n < 0)
		i++;
	c = malloc (i + 1);
	if (!c)
		return (NULL);
	c[i] = '\0';
	if (nb < 0)
	{
		c[0] = '-';
		nb *= -1;
	}
	if (nb == 0)
		c[0] = '0';
	while (nb > 0)
	{
		c[--i] = (nb % 10) + '0';
		nb /= 10;
	}
	return (c);
}
