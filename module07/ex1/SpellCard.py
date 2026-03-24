from ex0.Card import Card


class SpellCard(Card):
    VALID_EFFECTS = ["damage", "heal", "buff", "debuff"]

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        if effect_type in self.VALID_EFFECTS:
            self.effect_type = effect_type
        else:
            raise ValueError("Not a valid effect.")
        if self.effect_type == "damage":
            self.effect = "Deal 3 damage to target"
        elif self.effect_type == "heal":
            self.effect = "Heal 3 life points to target"
        elif self.effect_type == "buff":
            self.effect = "Buffed target's strenght"
        else:
            self.effect = "Debuffed target's strenght"
        self.type = "Spell"

    def play(self, game_state: dict) -> dict:
        game_state[self.name] = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }
        return game_state[self.name]

    def resolve_effect(self, targets: list) -> dict:
        results = {}
        for target in targets:
            if "target's" in self.effect:
                text = self.effect.replace("target's", target)
            elif "target" in self.effect:
                text = self.effect.replace("target", target)
            print(f"{self.effect}")
            results[target] = text
        return results
