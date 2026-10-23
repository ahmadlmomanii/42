/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 18:29:27 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 18:42:23 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

static int	is_sp(char c)
{
	return (c == ' ' || c == '\t' || c == '\n' || c == '\r' || c == '\v'
		|| c == '\f');
}

static int	countnums(const char *s)
{
	int	i;
	int	nums;

	i = 0;
	nums = 0;
	while (s[i])
	{
		while (s[i] && is_sp(s[i]))
			i++;
		if (s[i])
		{
			nums++;
			while (s[i] && !is_sp(s[i]))
				i++;
		}
	}
	return (nums);
}

static char	*copynums(const char *s, int start, int end)
{
	char	*res;
	int		i;

	res = malloc((end - start) + 1);
	if (!res)
		return (NULL);
	i = 0;
	while (start < end)
		res[i++] = s[start++];
	res[i] = '\0';
	return (res);
}

static int	fill_split(char **res, const char *s)
{
	int	i;
	int	j;
	int	start;

	i = 0;
	j = 0;
	while (s[i])
	{
		while (s[i] && is_sp(s[i]))
			i++;
		if (!s[i])
			break ;
		start = i;
		while (s[i] && !is_sp(s[i]))
			i++;
		res[j] = copynums(s, start, i);
		if (!res[j])
		{
			res[j] = NULL;
			return (ft_free_split(res), 0);
		}
		j++;
	}
	res[j] = NULL;
	return (1);
}

char	**ft_split(char const *s)
{
	char	**res;

	if (!s)
		error_exit();
	res = malloc(sizeof(char *) * (countnums(s) + 1));
	if (!res)
		error_exit();
	if (!fill_split(res, s))
		error_exit();
	return (res);
}
