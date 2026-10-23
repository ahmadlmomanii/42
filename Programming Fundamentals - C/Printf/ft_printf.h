/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 19:22:06 by aal-moum          #+#    #+#             */
/*   Updated: 2026/01/27 19:22:14 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdarg.h>

unsigned int	ft_putunsigned(unsigned int n);
int				ft_printf(const char *str, ...);
int				ft_putstr(char *s);
int				ft_putchar(char c);
int				ft_putnbr(int n);
int				ft_puthex(unsigned long n, char c);
int				ft_putptr(unsigned long n);

#endif
