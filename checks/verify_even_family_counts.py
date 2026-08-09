#!/usr/bin/env python3
"""Exact arithmetic replay for the audited even-degree family count."""


def count(k: int, ell: int) -> int:
    if k < 2 or k % 2:
        raise ValueError("k must be even and at least 2")
    if ell < 3:
        raise ValueError("ell must be at least 3")
    d = k // 2
    m = ell - 1
    one_active = m * (d - 1)
    two_active = m
    total = (
        one_active * (k // 2) * k ** (m - 1)
        + two_active * (k // 2) ** 2 * k ** (m - 2)
    )
    formula_numerator = m * (k - 1) * k**m
    assert formula_numerator % 4 == 0
    formula = formula_numerator // 4
    assert total == formula
    return total


def main() -> None:
    cases = [(2, 3), (2, 10), (4, 7), (6, 6), (8, 6)]
    for k, ell in cases:
        total = count(k, ell)
        conjectural = k**ell
        violation = total > conjectural
        expected = (ell - 1) * (k - 1) > 4 * k
        assert violation == expected
        print(
            f"k={k}; l={ell}; family_count={total}; "
            f"k^l={conjectural}; strict_violation={'YES' if violation else 'NO'}"
        )
    print("AUDITED_FAMILY_COUNT_REPLAY=PASS")


if __name__ == "__main__":
    main()
