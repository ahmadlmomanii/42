class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def raise_Plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_Water() -> None:
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        raise_Plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print("\nTesting WaterError...")
    try:
        raise_Water()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("\nTesting catching all garden errors...")
    try:
        raise_Plant()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raise_Water()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
