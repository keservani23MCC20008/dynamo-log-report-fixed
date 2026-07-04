import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load_report():
    """Helper: load /app/report.json as a dict (fails clearly if missing/invalid)."""
    assert REPORT.exists(), "no /app/report.json found"
    with REPORT.open() as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json must contain a single JSON object"
    return data


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and is a single valid JSON object."""
    _load_report()


def test_total_requests():
    """Criterion 2: total_requests equals the number of non-empty log lines (6)."""
    data = _load_report()
    assert data.get("total_requests") == 6, f"total_requests wrong: {data.get('total_requests')!r}"


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs (3)."""
    data = _load_report()
    assert data.get("unique_ips") == 3, f"unique_ips wrong: {data.get('unique_ips')!r}"


def test_top_path():
    """Criterion 4: top_path is the most frequently requested path (/index.html)."""
    data = _load_report()
    assert data.get("top_path") == "/index.html", f"top_path wrong: {data.get('top_path')!r}"
