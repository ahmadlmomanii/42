import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inv: dict[str, int] = {}
    for av in sys.argv[1:]:
        if ":" not in av:
            print(f"Error - invalid parameter '{av}'")
            continue
        if av.count(":") != 1:
            print(f"Error - invalid parameter '{av}'")
            continue
        item, quantity = av.split(":")
        if item in inv:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            conv_quantity: int = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue
        inv[item] = conv_quantity
    if not inv:
        print("Got inventory: {}")
        return
    print(f"Got inventory: {inv}")
    items_list = list(inv.keys())
    print(f"Item list: {items_list}")
    x = 0
    y = 0
    for i in inv:
        x = x + inv[i]
        y = y + 1
    print(f"Total quantity of the {y} items: {x}")
    most = items_list[0]
    least = items_list[0]
    for i in inv:
        if inv[i] > inv[most]:
            most = i
        if inv[i] < inv[least]:
            least = i
    if x == 0:
        print("Cannot calculate percentages: total quantity is 0")
    else:
        for i in inv:
            print(f"fItem {i} represents {inv[i] / x * 100:.1f}%")
    print(f"Item most abundant: {most} with quantity {inv[most]}")
    print(f"Item least abundant: {least} with quantity {inv[least]}")
    inv.update({"magic_item": 1})
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    main()
