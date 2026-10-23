/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 18:29:27 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 18:42:23 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

static int	is_space(char c)
{
	return (c == ' ' || c == '\t' || c == '\n' || c == '\r' || c == '\v'
		|| c == '\f');
}

static int	is_digit(char c)
{
	return (c >= '0' && c <= '9');
}

static const char	*parse_core(const char *s, long long *val, int *sign)
{
	while (*s && is_space(*s))
		s++;
	*sign = 1;
	if (*s == '+' || *s == '-')
	{
		if (*s == '-')
			*sign = -1;
		s++;
	}
	if (!is_digit(*s))
		error_exit();
	*val = 0;
	while (is_digit(*s))
	{
		*val = *val * 10 + (*s - '0');
		if (*sign == 1 && *val > INT_MAX)
			error_exit();
		if (*sign == -1 && -(*val) < INT_MIN)
			error_exit();
		s++;
	}
	return (s);
}

int	ft_atoi_strict(const char *s)
{
	long long	val;
	int			sign;

	if (!s || *s == '\0')
		error_exit();
	s = parse_core(s, &val, &sign);
	while (*s && is_space(*s))
		s++;
	if (*s != '\0')
		error_exit();
	return ((int)(val * sign));
}
