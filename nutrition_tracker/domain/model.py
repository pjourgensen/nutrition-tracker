from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Consumable:
    name: str
    calories: int
    carbs: int
    fat: int
    protein: int


class Log:
    def __init__(self, consumables: list[Consumable]):
        self._consumables = consumables

    def add(self, consumable: Consumable) -> None:
        self._consumables.append(consumable)

    def get(self) -> list[Consumable]:
        return self._consumables

    def summarize(self) -> dict:
        return {
            "calories": sum([c.calories for c in self._consumables]),
            "carbs": sum([c.carbs for c in self._consumables]),
            "fat": sum([c.fat for c in self._consumables]),
            "protein": sum([c.protein for c in self._consumables]),
        }
