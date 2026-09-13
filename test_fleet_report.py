# test_fleet_report.py
from fleet_report import fleet_summary

SAMPLE = [
    {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    {"id": "VOS-2210", "odometer": 48400, "last_service_km": 45000},
]


def test_summary_counts_due_cars():
    # Only VOS-4471 is nearly worn, so exactly one car is due.
    assert fleet_summary(SAMPLE)["due"] == 1


def test_summary_does_not_crash_on_missing_reading():
    # A car with no "last_service_km" must not crash fleet_summary.
    fleet_with_gap = [
        {"id": "VOS-7788", "odometer": 92000},
        {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    ]
    result = fleet_summary(fleet_with_gap)
    assert result["count"] == 2
    assert result["due"] == 1    # only VOS-4471 is worn; VOS-7788 has no reading so it is not flagged
