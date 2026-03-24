def archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    new_txt = "new_discovery.txt"
    print(f"Initializing new storage unit: {new_txt}")
    file = open(new_txt, "w")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    entry1 = "[ENTRY 001] New quantum algorithm discovered"
    entry2 = "[ENTRY 002] Efficiency increased by 347 %"
    entry3 = "[ENTRY 003] Archived by Data Archivist trainee"
    print(entry1)
    print(entry2)
    print(entry3)
    file.write(entry1 + "\n")
    file.write(entry2 + "\n")
    file.write(entry3 + "\n")
    print("\nData inscription complete. Storage unit sealed.")
    file.close()
    print(f"Archive '{new_txt}' ready for long-term preservation.")


if __name__ == "__main__":
    archive_creation()
