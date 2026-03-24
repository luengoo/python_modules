def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    confirmation = validate_ingredients(ingredients)
    if confirmation == f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({confirmation})"
    else:
        return f"Spell rejected: {spell_name} ({confirmation})"
