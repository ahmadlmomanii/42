import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    l: int = len(sys.argv)
    if l > 1:
        print(f"Arguments received: {l - 1}")
        for i in range(1, l):
            print(f"Argument {i}: {sys.argv[i]}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {l}")


def main() -> None:
    command_quest()


if __name__ == "__main__":
    main()
