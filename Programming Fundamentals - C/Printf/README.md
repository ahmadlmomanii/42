*This activity has been created as part of the 42 curriculum by aal-moum*

<h2>                   Description                 <h2/>

<p> printf is a standard function in C by the standard library stdio.h , the project was that the students recreats the printf function only using
malloc, free,  write, va_start, va_arg, va_copy, va_end.
the goal was to achieve excellent understanding of the function and learn some of the stdarg.h functions. <p/>

<h2>                   Instructions               <h2/>

<h3>                   Compilation                 <h3/>

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/libft.git
    cd libft
    ```

2. Compile the library by running the following command:
    ```bash
    make
    ```
    This will compile the library and generate the `libftprintf.a` static library file.

<h3>                  Installation               <h3/>

- To use the library in your project, simply copy or link the `libftprintf.a` file into your project directory.
- Add the path to `libftprintf.a` in your compilation commands. For example:
    ```bash
    gcc -o your_program your_program.c -L/path/to/libft -lft
    ```

<h2>                     Resources                <h2/>

1. the printf manual page in Lunix terminal
2. the home page for GNU  <a herf="https://www.gnu.org/software/coreutils/printf"> GNU.org<a/>
