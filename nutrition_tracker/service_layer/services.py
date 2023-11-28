from nutrition_tracker.domain.model import Consumable, Log


def log_consumable(log: Log, consumable: Consumable) -> None:
    log.add(consumable)
