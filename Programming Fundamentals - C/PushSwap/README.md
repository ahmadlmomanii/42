*This activity has been created as part of the 42 curriculum by aal-moum, atahtamo.*

# 🚀 Push Swap

## 📌 Description

Push Swap is a project from the 42 curriculum that focuses on sorting a list of integers using two stacks (**a** and **b**) and a limited set of operations.

The goal is to sort the input in ascending order while minimizing the number of operations performed.

## 🧠 Project Focus

This project emphasizes:

* Algorithmic thinking
* Optimization
* Data structures (linked lists / stacks)
* Complexity analysis

---

## ⚙️ Instructions

### 🔨 Compilation

```bash
make
```

### 🧹 Cleaning

```bash
make clean     # Remove object files
make fclean    # Remove executable
make re        # Rebuild project
```

### ▶️ Execution

```bash
./push_swap [numbers...]
```

### Examples

```bash
./push_swap 3 2 1
./push_swap "3 2 1"
./push_swap "1 2" 3
```

---

## 📊 Benchmark Mode

```bash
./push_swap --bench 3 2 1
```

### Displays:

* Disorder percentage
* Selected strategy
* Operation count

---

## 🧠 Algorithm Choices & Justification

This implementation uses multiple sorting strategies and dynamically selects the most appropriate one based on the input size and structure.

### 🔹 Simple Sort — O(n²)

Used for:

* Small datasets (e.g. ≤ 5 numbers)

### 🔹 Medium Sort

Used for:

* Moderate input sizes
* Balances performance and simplicity

### 🔹 Complex Sort

Used for:

* Large datasets
* Focuses on minimizing operations using advanced strategies

---

## 📊 Strategy Selection

Based on this:

| Disorder | Strategy |
| -------- | -------- |
| < 20%    | Simple   |
| < 50%    | Medium   |
| ≥ 50%    | Complex  |

### Justification

* Avoids using heavy algorithms unnecessarily
* Improves performance on partially sorted inputs
* Provides dynamic optimization

---

## 🛡️ Error Handling

The program handles:

* Invalid characters
* Overflow / underflow
* Duplicate numbers
* Empty input
* Incorrect formatting

### Output

```bash
Error
```

---

## 📈 Performance

| Input Size | Operations |
| ---------- | ---------- |
| 100        | ~555       |
| 500        | ~5380      |

Within the required limits for evaluation.

---

## 🛠️ Allowed Operations

### Stack A → B

* `pb` : push from a to b

### Stack B → A

* `pa` : push from b to a

### Swap

* `sa` : swap top of a
* `sb` : swap top of b
* `ss` : sa + sb

### Rotate

* `ra` : rotate a
* `rb` : rotate b
* `rr` : ra + rb

### Reverse Rotate

* `rra` : reverse rotate a
* `rrb` : reverse rotate b
* `rrr` : rra + rrb

---

## 📈 Goals

* Sort efficiently with the minimum number of operations
* Handle edge cases (duplicates, invalid input, overflow)
* Optimize for different input sizes

---

## 📚 Resources

### 📖 References

* 42 Subject (Push Swap)
* Stack data structure documentation
* Radix sort algorithm
* Fisher–Yates shuffle (for testing)
* Complexity analysis resources

---

## 🤖 AI Usage

AI tools (such as ChatGPT) were used for:

* Code review and debugging assistance
* Understanding algorithm optimizations
* Clarifying theoretical concepts
* Improving documentation quality

All implementation and logic decisions were written and validated manually.

---

## 👨‍💻 Authors

* aal-moum
* atahtamo

