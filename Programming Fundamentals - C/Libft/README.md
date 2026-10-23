*This project has been created as part of the 42 curriculum by Ahmad.*

# Libft

## Description
Libft is a custom C library created as part of the 42 curriculum.
The goal of this project is to reimplement essential standard C library functions from scratch in order to gain a deeper understanding of memory management, string manipulation, linked lists, and general low-level programming logic.  
The library provides a collection of functions that can be reused across future 42 projects and personal C applications.

## Instructions

### Compilation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/libft.git
    cd libft
    ```

2. Compile the library by running the following command:
    ```bash
    make
    ```
    This will compile the library and generate the `libft.a` static library file.

3. If you want to clean up object files and other temporary files generated during compilation, you can run:
    ```bash
    make clean
    ```

4. To remove the `libft.a` static library and clean all object files, run:
    ```bash
    make fclean
    ```

5. To recompile the library (after running `make fclean` or if you want to recompile), you can use:
    ```bash
    make re
    ```

### Installation

- To use the library in your project, simply copy or link the `libft.a` file into your project directory.
- Add the path to `libft.a` in your compilation commands. For example:
    ```bash
    gcc -o your_program your_program.c -L/path/to/libft -lft
    ```

### Usage

After compiling, the functions in the `libft` library are ready to be used in your project. Just include the `libft.h` header at the top of your C files where you want to use the library functions:

```c
#include "libft.h"

## Resources

### Classic References

- **The C Programming Language** by Brian W. Kernighan and Dennis M. Ritchie (2nd Edition)  
  This is the definitive book for learning C programming and understanding the core concepts, which are essential for the implementation of the `libft` functions.

- **C Standard Library Documentation**  
  - [C Standard Library - ISO/IEC 9899](https://en.wikipedia.org/wiki/C_standard_library)  
  - [GNU C Library Documentation](https://www.gnu.org/software/libc/manual/)  
  These sources provide detailed documentation on the functions used in the `libft` library and can be a helpful reference when implementing or optimizing your own functions.

- **"Learn C the Hard Way"** by Zed A. Shaw  
  An excellent tutorial series that focuses on C programming fundamentals and practical examples. It's a great resource if you're learning C from scratch.

- **Stack Overflow**  
  The **[Stack Overflow](https://stackoverflow.com/)** community is invaluable when debugging or searching for solutions to common issues related to C programming and library development.

- **C Programming Wiki**  
  [C Wiki](https://en.wikibooks.org/wiki/C_Programming) - A beginner-friendly tutorial covering C programming basics, common functions, and best practices.

- **man pages**  
  The Unix `man` command provides the manual entries for system functions, including the standard C library functions. Use `man <function_name>` to view detailed information about system functions like `malloc`, `free`, `strlen`, etc.

### Articles & Tutorials

- **[TutorialsPoint: C Programming](https://www.tutorialspoint.com/cprogramming/index.htm)**  
  A comprehensive guide that walks through C programming concepts and standard libraries in detail.

- **[GeeksforGeeks: C Programming](https://www.geeksforgeeks.org/c-programming-language/)**  
  A platform with a variety of C programming tutorials, challenges, and solutions that can be useful when learning the intricacies of C.

- **[Learn-C.org](https://www.learn-c.org/)**  
  A free interactive tutorial that covers the basics of C and helps new developers get started with the language.

- **[Understanding `malloc` and Memory Allocation](https://www.gnu.org/software/libc/manual/html_node/Memory-Allocation.html)**  
  An article by the GNU Project that explains memory management in C, a crucial concept for implementing functions like `ft_malloc`, `ft_free`, and memory-related utilities in `libft`.

### AI Usage

In this `libft` project, **AI-assisted tools** were used to help with the following tasks:

1. **Code Review & Optimization**  
   AI was used to analyze the written functions and suggest possible optimizations. For example, it assisted in improving the performance of certain string manipulation functions (such as `ft_strcpy` and `ft_strcat`) by recommending more efficient memory usage strategies or algorithmic improvements.

2. **Functionality Testing**  
   AI tools were leveraged to automatically generate test cases for edge cases that could have been missed, such as testing memory overflows, invalid inputs, and boundary conditions in functions like `ft_memcpy` and `ft_memset`. This automated testing helped ensure the robustness of the library.

3. **Documentation & Commenting**  
   AI-assisted documentation tools were employed to generate initial docstrings and comments for each function, ensuring that the codebase remains well-documented and readable. This was especially helpful for functions that involve intricate memory manipulation or pointer arithmetic, where clarity is essential.

4. **Code Style Enforcement**  
   AI-powered linters were used to enforce consistent code styling (e.g., indentation, naming conventions) according to the project's coding standards. This helped maintain uniformity and readability throughout the project.

5. **Refactoring Suggestions**  
   In cases where certain functions were overly complicated or could benefit from a simpler approach, AI tools suggested refactoring strategies to improve both performance and maintainability without altering the intended functionality.

While AI was instrumental in suggesting improvements and providing testing insights, the actual implementation, design decisions, and algorithmic choices were made by the developer to maintain the integrity and educational value of the project.
