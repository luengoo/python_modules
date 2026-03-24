def storage_access() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file_name}")
    try:
        file = open(file_name, "r")
        message = file.read()
        print("Connection established, lets recover the data...\n")
        print("RECOVERED DATA:")
        print(message)
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except Exception:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    storage_access()
