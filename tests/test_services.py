from nutrition_tracker.domain.model import Consumable, Log
from nutrition_tracker.service_layer.services import log_consumable


def test_can_log_consumable() -> None:
    log = Log([])
    consumable = Consumable(
        name="apple",
        calories=52,
        carbs=13,
        fat=0,
        protein=0,
    )
    log_consumable(log, consumable)
    assert log.get() == [consumable]