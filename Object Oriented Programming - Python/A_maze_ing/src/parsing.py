import os
import sys
import random


def check_config(values: tuple[int, int, tuple[int, int],
                               tuple[int, int], int, bool, str]) -> None:
    """Validate the maze configuration values.

    Args:
        values: Tuple containing the maze width, height, entry position,
            exit position, seed, perfect-maze flag, and output filename.

    Raises:
        ValueError: If any configuration value is invalid.
    """
    width, height, start, end, seed, perfect, output = values
    if height < 1:
        raise ValueError("The height should be more than 0")
    if width < 1:
        raise ValueError("The width should be more than 0")
    if height < 7 or width < 9:
        raise ValueError("the maze is smaller than the minimum size (7 * 9)")
    if width == 1 and height == 1:
        raise ValueError("The 1*1 will not make a maze")
    if start == end:
        raise ValueError("The entry and exit should be different")
    if not (0 <= start[0] < height and 0 <= start[1] < width):
        raise ValueError("Entry is out of the maze")
    if not (0 <= end[0] < height and 0 <= end[1] < width):
        raise ValueError("Exit is out of the maze")
    if not perfect:
        if width == 1 or height == 1:
            raise ValueError(
                "There is just one path and it is not pacman usable"
            )
        if width == 2 and height == 2:
            raise ValueError("2 * 2 is not pacman usable")
    if not output:
        raise ValueError("Put a valid name for output file")
    terminal_size = os.get_terminal_size()
    if terminal_size[0] < (width * 4.1) or terminal_size[1] < (height * 2 + 6):
        raise ValueError(
            f"terminal size is to small to fit the maze: {
                terminal_size[0], terminal_size[1]}")


def load_config() -> tuple[int, int, tuple[int, int],
                           tuple[int, int], int, bool, str]:
    """Load and validate the maze configuration from config.txt.

    Returns:
        A tuple containing the maze width, height, entry position,
        exit position, seed, perfect-maze flag, and output filename.

    Raises:
        SystemExit: If the configuration file is missing, invalid,
            or cannot be read.
    """
    try:
        if len(sys.argv) < 2:
            print("Error: Missing argument.")
            exit()
        elif len(sys.argv) > 2:
            print("Error: there is too many arguments.")
        required = [
            "WIDTH", "HEIGHT", "ENTRY",
            "EXIT", "OUTPUT_FILE", "PERFECT"
        ]
        configs: dict[str, str] = {}
        if not os.path.isfile(sys.argv[1]):
            raise ValueError("config file does not exist")
        try:
            file = open(sys.argv[1], "r")
        except OSError as e:
            raise ValueError("Cannot open config file") from e
        line_number = 0
        for line in file:
            if line.strip().startswith("#"):
                continue
            line_number += 1
            line = line.strip()
            if not line:
                continue
            if line.count("=") != 1:
                raise ValueError(
                    f"Invalid line {line_number}: use KEY=VALUE"
                )
            key, value = line.split("=")
            key = key.strip().upper()
            value = value.strip()
            if not key:
                raise ValueError(
                    f"Invalid variable at line {line_number}"
                )
            if key not in required and key != "SEED":
                raise ValueError(f"Unknown variable: {key}")
            if key in configs:
                raise ValueError(f"Duplicate variable: {key}")
            if not value:
                raise ValueError(f"{key} cannot be empty")
            configs[key] = value
        file.close()
        for key in required:
            if key not in configs:
                raise ValueError(f"Missing variable: {key}")
        try:
            width = int(configs["WIDTH"])
            height = int(configs["HEIGHT"])
        except ValueError as e:
            raise ValueError(
                "Width and Height must be numbers"
            ) from e
        if "SEED" in configs:
            try:
                seed = int(configs["SEED"])
            except ValueError as e:
                raise ValueError("Seed must be a number") from e
        else:
            seed = random.randint(0, 1000)
        entry = configs["ENTRY"].split(",")
        exit_position = configs["EXIT"].split(",")
        if len(entry) != 2:
            raise ValueError("Entry must contain two numbers")
        if len(exit_position) != 2:
            raise ValueError("Exit must contain two numbers")
        try:
            start = (int(entry[0].strip()), int(entry[1].strip()))
            end = (
                int(exit_position[0].strip()),
                int(exit_position[1].strip())
            )
        except ValueError as e:
            raise ValueError(
                "Entry and Exit must contain numbers"
            ) from e
        perfect_value = configs["PERFECT"].lower()
        if perfect_value == "true":
            perfect = True
        elif perfect_value == "false":
            perfect = False
        else:
            raise ValueError("Perfect must be True or False")
        output = configs["OUTPUT_FILE"].strip()
        start = (start[1], start[0])
        end = (end[1], end[0])
        values = (
            width, height, start, end, seed, perfect, output
        )
        check_config(values)
        return values
    except (ValueError, OSError) as e:
        print(f"Config error: {e}")
        raise SystemExit(0)
