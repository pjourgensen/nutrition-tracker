from nutrition_tracker.domain.model import Consumable, Log


def test_can_log_consumable() -> None:
    log = Log([])
    consumable = Consumable(
        name="apple",
        calories=52,
        carbs=13,
        fat=0,
        protein=0,
    )
    log.add(consumable)
    assert log.get() == [consumable]


def test_can_summarize_log() -> None:
    log = Log([
        Consumable(
            name="apple",
            calories=52,
            carbs=13,
            fat=0,
            protein=0,
        ),
        Consumable(
            name="banana",
            calories=89,
            carbs=23,
            fat=0,
            protein=1,
        ),
    ])
    summary = log.summarize()
    assert summary == {
        "calories": 141,
        "carbs": 36,
        "fat": 0,
        "protein": 1,
    }
