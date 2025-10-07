from __future__ import annotations

import math
import re
from typing import Optional, Tuple


COMPARATOR_PATTERN = re.compile(r"^(<=|>=|=|<|>){0,1}\s*([0-9]+(?:\.[0-9]+)?)\s*")


def parse_numeric(value: object) -> Optional[float]:
    """Parse a value into float, returning None for NaN/invalid."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
            return None
        return float(value)
    if isinstance(value, str):
        raw = value.strip()
        if raw.lower() == "nan":
            return None
        # Extract leading numeric portion, e.g. "389 kcal" -> 389
        m = re.search(r"([0-9]+(?:\.[0-9]+)?)", raw)
        if not m:
            return None
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


def parse_comparator(expr: Optional[str]) -> Optional[Tuple[str, float]]:
    """Parse comparator expressions like ">=4.5", "<= 400", "=30", "40" (implies =).

    Returns (op, value) where op in {"<=", ">=", "<", ">", "="}.
    Returns None if expr is falsy or cannot be parsed.
    """
    if not expr:
        return None

    expr = expr.strip()
    m = COMPARATOR_PATTERN.match(expr)
    if not m:
        # Try to parse as bare numeric
        value = parse_numeric(expr)
        if value is None:
            return None
        return ("=", value)

    op = m.group(1) or "="
    try:
        value = float(m.group(2))
    except ValueError:
        return None
    return (op, value)


def compare_value(candidate: Optional[float], comp: Tuple[str, float]) -> bool:
    """Return True if candidate satisfies comparator (op, value). None never matches."""
    if candidate is None:
        return False
    op, target = comp
    if op == "<":
        return candidate < target
    if op == "<=":
        return candidate <= target
    if op == ">":
        return candidate > target
    if op == ">=":
        return candidate >= target
    # default '=' exact match
    return candidate == target


def extract_calories(nutrients: object) -> Optional[float]:
    """Extract numeric calories from a nutrients object or string."""
    if nutrients is None:
        return None
    if isinstance(nutrients, dict):
        calories_val = nutrients.get("calories") or nutrients.get("calorie")
    else:
        calories_val = str(nutrients)
    return parse_numeric(calories_val)
