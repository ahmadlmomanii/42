/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   put.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 16:21:08 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	ft_putdouble_fd(double n, int fd)
{
	long	integral;
	long	fractional;

	if (n < 0)
	{
		write(fd, "-", 1);
		n = -n;
	}
	integral = (long)n;
	n -= (double)integral;
	fractional = (long)(n * 100 + 0.5);
	if (fractional == 100)
	{
		integral++;
		fractional = 0;
	}
	ft_putnbr_fd(integral, fd);
	write(fd, ".", 1);
	if (fractional < 10)
		write(fd, "0", 1);
	ft_putnbr_fd(fractional, fd);
}

void	ft_putnbr_fd(long n, int fd)
{
	char	c;

	if (n < 0)
	{
		write(fd, "-", 1);
		n = -n;
	}
	if (n >= 10)
		ft_putnbr_fd(n / 10, fd);
	c = (n % 10) + '0';
	write(fd, &c, 1);
}
