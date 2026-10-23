# 42 Common Core Journey

A collection of projects and exercises completed as part of my journey at **42 Irbid**. This repository documents my progress through the 42 curriculum, with a focus on low-level programming, algorithms, Python, Linux system administration, and computer networking.

> **Status:** In progress — this repository will continue to grow as I work through more projects in the 42 Common Core.

## Table of Contents

- [About](#about)
- [Projects](#projects)
  - [Programming Fundamentals — C](#programming-fundamentals--c)
  - [Object-Oriented Programming — Python](#object-oriented-programming--python)
  - [Systems and Network Administration](#systems-and-network-administration)
- [Skills and Technologies](#skills-and-technologies)
- [Repository Structure](#repository-structure)
- [How to Explore](#how-to-explore)
- [Disclaimer](#disclaimer)

## About

42 is a project-based programming school where students learn through practical assignments, peer evaluation, and independent problem-solving. This repository brings together selected projects and exercises I have completed so far.

The goal is to keep my work organized, track my progress, and demonstrate the concepts I am learning through hands-on implementation. Individual project folders may contain their own README files with more specific explanations and instructions.

## Projects

### Programming Fundamentals — C

Projects focused on C programming, memory management, data structures, parsing, and algorithmic problem-solving.

| Project | Description | Topics |
|---|---|---|
| [Libft](./Programming%20Fundamentals%20-%20C/Libft/) | A personal C library that reimplements a selection of standard C library functions and additional utility functions. | Pointers, strings, memory management, linked lists |
| [ft_printf](./Programming%20Fundamentals%20-%20C/Printf/) | A custom implementation of `printf` and supported format conversions. | Variadic functions, formatting, output handling |
| [get_next_line](./Programming%20Fundamentals%20-%20C/GetNextLine/) | Reads a file descriptor line by line. | File descriptors, static variables, buffered I/O, memory allocation |
| [push_swap](./Programming%20Fundamentals%20-%20C/PushSwap/) | Sorts integer inputs using two stacks and a limited set of operations. | Stack operations, parsing, sorting strategies, algorithm optimization |

### Object-Oriented Programming — Python

A collection of Python Piscine exercises covering Python fundamentals, object-oriented design, exceptions, modules, data processing, and validation.

Main exercise collections currently included:

| Collection | Focus | Location |
|---|---|---|
| GardenGuardian | Exception handling and custom errors | [Open folder](./Object%20Oriented%20Programming%20-%20Python/PythonPiscine/GardenGuardian/) |
| TheCodex | Modules, packages, and object organization | [Open folder](./Object%20Oriented%20Programming%20-%20Python/PythonPiscine/TheCodex/) |
| CodeNexus | Data processors, streams, and pipelines | [Open folder](./Object%20Oriented%20Programming%20-%20Python/PythonPiscine/CodeNexus/) |
| DataDeck | Classes, factories, capabilities, and strategy patterns | [Open folder](./Object%20Oriented%20Programming%20-%20Python/PythonPiscine/DataDeck/) |
| TheMatrix | Configuration and external data handling | [Open folder](./Object%20Oriented%20Programming%20-%20Python/PythonPiscine/TheMatrix/) |
| CosmicData | Structured data and model validation | [Open folder](./Object%20Oriented%20Programming%20-%20Python/PythonPiscine/CosmicData/) |
| Additional exercises | Other Python challenges and exercises from the curriculum | [Browse Python Piscine](./Object%20Oriented%20Programming%20-%20Python/PythonPiscine/) |

These exercises are organized by collection and exercise number. Refer to the source files in each directory for the specific task and implementation.

### Systems and Network Administration

Projects focused on understanding operating systems, system configuration, security practices, and network fundamentals.

| Project | Description | Topics |
|---|---|---|
| [Born2beroot](./Systems%20And%20Networks%20Administration/Born2beRoot/) | Linux virtual-machine setup and system-administration tasks. | Linux, users and groups, SSH, sudo, security, system monitoring |
| [NetPractice](./Systems%20And%20Networks%20Administration/NetPractice/) | Practical network-configuration exercises. | IPv4, subnet masks, routing, gateways, TCP/IP |

## Skills and Technologies

**Languages**
- C
- Python

**Tools and environments**
- Linux
- Git and GitHub
- GCC and Make
- Virtual machines

**Concepts practised**
- Pointers and dynamic memory allocation
- String manipulation and parsing
- File descriptors and buffered input/output
- Linked lists and stack-based algorithms
- Algorithm design and optimization
- Object-oriented programming
- Exceptions, modules, and packages in Python
- Data processing and validation
- IP addressing, subnetting, and routing
- Linux administration and basic system security

## Repository Structure

```text
.
├── Programming Fundamentals - C/
│   ├── Libft/
│   ├── Printf/
│   ├── GetNextLine/
│   └── PushSwap/
├── Object Oriented Programming - Python/
│   └── PythonPiscine/
│       ├── GardenGuardian/
│       ├── TheCodex/
│       ├── CodeNexus/
│       ├── DataDeck/
│       ├── TheMatrix/
│       ├── CosmicData/
│       └── ...
└── Systems And Networks Administration/
    ├── Born2beRoot/
    └── NetPractice/
```

## How to Explore

1. Choose a category above.
2. Open a project directory to review its source code and any project-specific documentation.
3. For C projects with a `Makefile`, check the project's README for its build instructions and requirements before compiling.
4. For Python exercises, check whether the exercise includes specific dependencies or execution instructions.

Project requirements and permitted functions can vary across the 42 curriculum. Use each project's own documentation as the source of truth for its setup and constraints.

## Disclaimer

This repository is a personal record of my learning and project work. It is **not an official 42 repository** and is not affiliated with or endorsed by 42. Project implementations are shared for educational and portfolio purposes. If you are also studying at 42, follow your campus rules and the academic-integrity requirements that apply to your curriculum.

---

*Still learning. Still building. One project at a time.*
