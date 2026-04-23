def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    artifacts.sort(key=lambda x: x["power"], reverse=True)
    return artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtred = list(filter(lambda x: x["power"] >= min_power, mages))
    return filtred


def spell_transform(spells: list[str]) -> list[str]:
    result = list(map(lambda x: "* " + x + " *", spells))
    return result


def mages_stats(mages: list[dict]) -> dict:
    max_power = list(max(lambda x: x["power"]))
    min_power = list(min(lambda x: x["power"]))
    mages_len = len(mages)
    avg_power = list(sum(lambda x: x["power"])) // mages_len
    return {
        'max_power': max_power, 'min_power': min_power, 'avg_power': avg_power}


def main():
    print("\nTesting artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92},
        {"name": "Serpent Teeth", "power": 12}
    ]
    spells = [
        "fireball",
        "heal",
        "shield"
    ]
    artifact_sorter(artifacts)
    print(f"{artifacts[0].get('name')} ({artifacts[0].get('power')} power) "
          f"comes before {artifacts[1].get('name')} "
          f"({artifacts[1].get('power')} power)\n")
    print("Testing spell transformer...")
    transformed = spell_transform(spells)
    for x in transformed:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    main()
