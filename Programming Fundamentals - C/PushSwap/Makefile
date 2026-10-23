NAME = push_swap

CC = cc
CFLAGS = -Wall -Wextra -Werror

SRC = main.c parsing.c build_stack_a.c check_duplicate.c error.c \
	ft_atoi.c ft_split.c ft_free_split.c ft_strcmp.c is_sorted.c \
	stack.c push.c swap.c rotate.c rev_rotate.c \
	select_strategy.c simple_sort.c sort_2_3_4_5.c \
	medium_sort.c medium_helper.c complex_sort.c \
	disorder.c bench.c put.c space_checker.c convert_stack.c \
	find_min.c index_for_ps.c sm_sort_selector.c

OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

%.o: %.c push_swap.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
