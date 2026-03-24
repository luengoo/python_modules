VALID_INGREDIENTS = {"fire", "water", "earth", "air"}


def validate_ingredients(ingredients: str) -> str:
    parts = ingredients.split()
    if all(p in VALID_INGREDIENTS for p in parts):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
