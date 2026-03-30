import sys
import os
import site

"""This is my first virtual environment exercise."""


def main():
    if sys.prefix != sys.base_prefix:
        """Compares the base system prefix and the current one"""
        print("\nMATRIX STATUS: Welcome to the construct\n")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current python: {sys.executable}")
    """sys.executable is used to give the python path that is being used"""
    print("Virtual environment: ", end="")

    venv = os.environ.get("VIRTUAL_ENV")
    """Here we get the venv path"""
    if venv:
        print(venv.split("/")[-1])
        """We get only the name of the venv using a negative indexer"""
        print(f"\nEnvironment path: {venv}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print(f"\nPackage instalation path:\n{site.getsitepackages()[0]}")
        """site.getsitepackages is used to give the site-packages path only"""
    else:
        print("None detected.")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\nScripts\nactivate  # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
