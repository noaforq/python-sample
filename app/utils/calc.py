from decimal import ROUND_HALF_UP, Decimal


def round_half_up(f: float) -> int:
    """四捨五入"""
    return int(Decimal(str(f)).quantize(Decimal("0"), rounding=ROUND_HALF_UP))
