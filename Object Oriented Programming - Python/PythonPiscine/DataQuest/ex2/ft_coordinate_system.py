import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates: str = input("Enter new coordinates"
                                 "as floats in format ’x,y,z’: ")
        spl_coordinates: list[str] = coordinates.split(',')
        check: bool = False
        if len(spl_coordinates) == 3:
            float_coordinates: list[float] = []
            for i in range(0, 3):
                try:
                    float_coordinates.append(float(spl_coordinates[i]))
                    check = True
                except ValueError as e:
                    check = False
                    print(f"Error on parameter '{spl_coordinates[i]}': {e}")
                    break
        else:
            print("Invalid syntax")
            continue
        if check:
            break
    tup_coordinates: tuple[float, float, float] = (
            float_coordinates[0],
            float_coordinates[1],
            float_coordinates[2]
            )
    return tup_coordinates


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    t1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {t1}")
    print(f"It includes: X={t1[0]}, Y={t1[1]}, Z={t1[2]}")
    d1: float = math.sqrt((t1[0]-0)**2 + (t1[1]-0)**2 + (t1[2]-0)**2)
    print(f"Distance to center: {d1:.4f}")
    print("\nGet a second set of coordinates")
    t2: tuple[float, float, float] = get_player_pos()
    d2: float = math.sqrt(
            (t2[0]-t1[0])**2 +
            (t2[1]-t1[1])**2 +
            (t2[2]-t1[2])**2
            )
    print(f"Distance between the 2 sets of coordinates: {d2:.4f}")


if __name__ == "__main__":
    main()
