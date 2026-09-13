# km_wachter.py
# KM-Waechter decides when a Vossberg Mobility car needs a service.
# Written in 2013. Nobody has cleaned it up since.

SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80


def wear_percent(km_since_service: float, interval: float) -> float:
    """Return the percentage of the service interval consumed."""
    ratio = km_since_service / interval   # true division: e.g. 14900/15000 = 0.9933
    return ratio * 100


def needs_service(car: dict) -> bool:
    """Return True when the car has consumed >= WARN_AT_PERCENT of its service interval."""
    last = car.get("last_service_km")
    if last is None:          # no reading → treat as freshly serviced, never flag
        return False
    km_since = car["odometer"] - last
    pct = wear_percent(km_since, SERVICE_INTERVAL_KM)
    return pct >= WARN_AT_PERCENT


def check_fleet(fleet: list[dict]) -> list:
    """Flag every car that needs service and return their ids."""
    flagged = []
    for car in fleet:
        if needs_service(car):
            flagged.append(car["id"])
            print(f"SERVICE DUE: {car['id']}")
    return flagged
