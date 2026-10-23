import importlib
import sys

packages = {"pandas": "Data manipulation ready",
            "numpy": "Numerical computation ready",
            "matplotlib": "Visualization ready"
            }

print("LOADING STATUS: Loading programs...\n")
print("Checking dependencies:")
missing = False
for package, description in packages.items():
    try:
        pack = importlib.import_module(package)
        print(f"[OK] {package} ({pack.__version__}) - {description}")
    except ImportError:
        missing = True
        print(f"[MISSING] {package} "
              f"- {description.replace('ready', 'unavailable')}")
if missing:
    print("\nInstall using pip:")
    print("pip install -r requirements.txt")
    print("\nOr using Poetry:")
    print("poetry install")
    sys.exit(1)


def main() -> None:
    import numpy
    import pandas
    import matplotlib.pyplot as plt
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    temp = numpy.random.randint(-20, 40, size=1000)
    print("Generating visualization...")
    data = pandas.DataFrame(temp, columns=["Temperature"])
    plt.plot(data["Temperature"])
    plt.title("Matrix Temperature")
    plt.xlabel("Sample")
    plt.ylabel("Temperature")
    plt.grid(True)
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
