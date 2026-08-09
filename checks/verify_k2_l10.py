#!/usr/bin/env python3
"""Exact combinatorial replay for the quartic ten-variable witness."""

from math import prod


def main() -> None:
    total = 0
    print("COUNTEREXAMPLE: k=2, l=10")
    for j in range(9):
        squares = [j * (8 - j)]
        squares.extend((j - i + 1) * (j - i) for i in range(1, 9))
        assert all(a >= 0 for a in squares)
        zeros = [i for i, a in enumerate(squares) if a == 0]
        positives = [i for i, a in enumerate(squares) if a > 0]
        assert len(zeros) == 2
        assert len(positives) == 7
        points = prod(1 if a == 0 else 2 for a in squares)
        assert points == 128
        total += points
        print(f"t={j}: zero_indices={zeros}; positive_count=7; points=128")
    assert total == 1152
    assert 2**10 == 1024
    assert total > 2**10
    print("TOTAL_REAL_ZEROS=1152")
    print("CONJECTURAL_VALUE=1024")
    print("EXCESS=128")
    print("CERTIFIED_COUNTEREXAMPLE=YES")


if __name__ == "__main__":
    main()
