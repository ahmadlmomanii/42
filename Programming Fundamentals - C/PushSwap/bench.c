/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 19:02:22 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 16:21:08 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	display_bench(t_ps *ps)
{
	write(2, "[bench] disorder: ", 19);
	ft_putdouble_fd(ps->bench.disorder * 100, 2);
	write(2, "%\n", 2);
	write(2, "[bench] strategy: ", 19);
	if (ps->is_adaptive == 1)
		adaptive(ps);
	else if (ps->flag == 1)
		write(2, "Simple / O(n^2)\n", 16);
	else if (ps->flag == 2)
		write(2, "Medium / O(n√n)\n", 18);
	else if (ps->flag == 3)
		write(2, "Complex / O(n log n)\n", 21);
	write(2, "[bench] total_ops: ", 20);
	ft_putnbr_fd(ps->bench.count, 2);
	write(2, "\n", 1);
	ops(ps);
}

void	ops(t_ps *ps)
{
	write(2, "[bench] sa: ", 12);
	ft_putnbr_fd(ps->bench.sa, 2);
	write(2, " sb: ", 5);
	ft_putnbr_fd(ps->bench.sb, 2);
	write(2, " ss: ", 5);
	ft_putnbr_fd(ps->bench.ss, 2);
	write(2, " pa: ", 5);
	ft_putnbr_fd(ps->bench.pa, 2);
	write(2, " pb: ", 5);
	ft_putnbr_fd(ps->bench.pb, 2);
	write(2, "\n", 1);
	write(2, "[bench] ra: ", 12);
	ft_putnbr_fd(ps->bench.ra, 2);
	write(2, " rb: ", 5);
	ft_putnbr_fd(ps->bench.rb, 2);
	write(2, " rr: ", 5);
	ft_putnbr_fd(ps->bench.rr, 2);
	write(2, " rra: ", 6);
	ft_putnbr_fd(ps->bench.rra, 2);
	write(2, " rrb: ", 6);
	ft_putnbr_fd(ps->bench.rrb, 2);
	write(2, " rrr: ", 6);
	ft_putnbr_fd(ps->bench.rrr, 2);
	write(2, "\n", 1);
}

void	adaptive(t_ps *ps)
{
	if (ps->bench.disorder < 0.2)
		write(2, "Adaptive / O(n^2)\n", 18);
	else if (ps->bench.disorder >= 0.2 && ps->bench.disorder < 0.5)
		write(2, "Adaptive / O(n√n)\n", 20);
	else
		write(2, "Adaptive / O(n log n)\n", 22);
}
