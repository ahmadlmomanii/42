/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   puthex.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 19:27:00 by aal-moum          #+#    #+#             */
/*   Updated: 2026/01/27 19:27:03 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

unsigned int	ft_putunsigned(unsigned int n)
{
	int	count;

	count = 0;
	if (n >= 10)
		count += ft_putunsigned(n / 10);
	count += ft_putchar((n % 10) + '0');
	return (count);
}

int	ft_puthex(unsigned long n, char c)
{
	char	*base;
	int		count;

	count = 0;
	if (c == 'X')
		base = "0123456789ABCDEF";
	else
		base = "0123456789abcdef";
	if (n >= 16)
		count += ft_puthex(n / 16, c);
	count += ft_putchar(base[n % 16]);
	return (count);
}

int	ft_putptr(unsigned long n)
{
	int	count;

	count = 0;
	if (n == 0)
		return (ft_putstr("(nil)"));
	count += ft_putstr("0x");
	count += ft_puthex(n, 'x');
	return (count);
}
