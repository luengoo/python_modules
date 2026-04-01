import sys
import importlib
from importlib.metadata import version, PackageNotFoundError


REQUIRED = {
    "pandas": "Data manipulation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready"
}


def check_dependencies():
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    missing = []

    for pkg, message in REQUIRED.items():
        try:
            importlib.import_module(pkg)
            v = version(pkg)
            print(f"[OK] {pkg} ({v}) - {message}")
        except (ImportError, PackageNotFoundError):
            print(f"[MISSING] {pkg}")
            missing.append(pkg)

    if missing:
        print("\nMissing dependencies detected.")
        print("Install with one of the following:\n")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)


def generate_matrix_data():
    import numpy as np
    import pandas as pd

    print("\nAnalyzing Matrix data...")

    data = np.random.randint(0, 100, size=(1000, 5))

    df = pd.DataFrame(
        data,
        columns=["Agent_A", "Agent_B", "Agent_C", "Agent_D", "Agent_E"]
    )

    print("Processing 1000 data points...")

    return df


def create_visualization(df):
    import matplotlib.pyplot as plt
    print("Generating visualization...")

    df.mean().plot(kind="bar", title="Matrix Signal Analysis")

    plt.xlabel("Agents")
    plt.ylabel("Average Signal Strength")
    plt.tight_layout()

    plt.savefig("matrix_analysis.png")


def main():
    check_dependencies()

    df = generate_matrix_data()

    create_visualization(df)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
