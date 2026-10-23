/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aal-moum <aal-moum@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 18:44:07 by aal-moum          #+#    #+#             */
/*   Updated: 2026/02/11 19:57:02 by aal-moum         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <limits.h>
# include <stdbool.h>
# include <stdlib.h>
# include <unistd.h>

/* ================= STRUCTS ================= */

typedef struct s_node
{
	int				data;
	struct s_node	*next;
}					t_node;

typedef struct s_bench
{
	int				sa;
	int				sb;
	int				ss;
	int				pa;
	int				pb;
	int				ra;
	int				rb;
	int				rr;
	int				rra;
	int				rrb;
	int				rrr;
	double			disorder;
	int				count;
}					t_bench;

typedef struct s_ps
{
	t_node			*a;
	t_node			*b;
	t_bench			bench;
	int				size_a;
	int				size_b;
	int				flag;
	bool			bench_on;
	bool			is_adaptive;
}					t_ps;

/* ================= PARSING ================= */

int					parsing(int ac, char **av, t_ps *ps);
void				build_stack_a(int i, char **av, t_ps *ps, int ac);
int					has_space(char *s);
int					ft_atoi_strict(const char *s);
int					ft_strcmp(const char *s1, const char *s2);
char				**ft_split(char const *s);
void				ft_free_split(char **arr);
void				dup_check(t_node *a);
void				error_exit(void);

/* ================= STACK ================= */

t_node				*new_node(int value);
void				node_add_back(t_node **a, t_node *new);
void				stack_free(t_node **a);
int					is_sorted(t_node *a);

/* ================= OPERATIONS ================= */

void				sa(t_ps *ps);
void				sb(t_ps *ps);
void				ss(t_ps *ps);
void				pa(t_ps *ps);
void				pb(t_ps *ps);
void				ra(t_ps *ps);
void				rb(t_ps *ps);
void				rr(t_ps *ps);
void				rra(t_ps *ps);
void				rrb(t_ps *ps);
void				rrr(t_ps *ps);

/* ================= SORTING ================= */

void				select_strategy(t_ps *ps);
void				execute_sort(t_ps *ps);

/* simple */
void				sort_simple(t_ps *ps);
void				sort_two(t_ps *ps);
void				sort_three(t_ps *ps);
void				sort_four(t_ps *ps);
void				sort_five(t_ps *ps);
int					find_min(t_ps *ps);
int					ra_or_rra(t_ps *ps, int min);
void				small_selector(t_ps *ps);

/* medium */
void				sort_medium(t_ps *ps);
void				push_and_rotate_a(int chunks, t_ps *ps);
void				push_and_rotate_b(t_ps *ps);
int					ft_sqrt(int n);
int					find_index(int *arr, int size, int data);
int					find_max(t_node *stack);
int					index_for_ps(t_node *a, int data);
int					position(t_node *stack, int value);
void				sort_array(int *arr, int size);

/* complex */
void				sort_complex(t_ps *ps);
int					get_max_bits(int max);
void				complex_helper(int max_bits, t_ps *ps, int size);
void				convert_stack(t_ps *ps);

/* ================= BENCH ================= */

double				compute_disorder(t_node *a, int size);
void				display_bench(t_ps *ps);
void				ops(t_ps *ps);
void				adaptive(t_ps *ps);
void				ft_putdouble_fd(double n, int fd);
void				ft_putnbr_fd(long n, int fd);

#endif
