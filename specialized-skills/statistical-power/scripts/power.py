#!/usr/bin/env python3
"""Approximate power and sample-size calculations using normal approximations (stdlib only).

These are planning estimates. Confirm important calculations with dedicated software
(for example G*Power, statsmodels, or R's pwr) and a statistician.
"""

import argparse
import math
from statistics import NormalDist

_NORMAL = NormalDist()


def _check_probability(name, value):
    if not 0 < value < 1:
        raise ValueError(f"{name} must be between 0 and 1 (exclusive)")


def n_per_group_means(effect_size, alpha=0.05, power=0.8, two_sided=True):
    """Per-group n for a two-sample comparison of means; effect_size is Cohen's d.

    Uses the normal approximation with Guenther's small-sample correction.
    """
    _check_probability("alpha", alpha)
    _check_probability("power", power)
    if effect_size == 0:
        raise ValueError("effect size must be non-zero")
    z_alpha = _NORMAL.inv_cdf(1 - alpha / (2 if two_sided else 1))
    z_power = _NORMAL.inv_cdf(power)
    n = 2 * ((z_alpha + z_power) / abs(effect_size)) ** 2 + z_alpha**2 / 4
    return math.ceil(n)


def power_means(n_per_group, effect_size, alpha=0.05, two_sided=True):
    """Approximate power of a two-sample comparison of means for a given per-group n."""
    _check_probability("alpha", alpha)
    if n_per_group < 2:
        raise ValueError("n per group must be at least 2")
    z_alpha = _NORMAL.inv_cdf(1 - alpha / (2 if two_sided else 1))
    noncentrality = abs(effect_size) * math.sqrt(n_per_group / 2)
    power = 1 - _NORMAL.cdf(z_alpha - noncentrality)
    if two_sided:
        power += _NORMAL.cdf(-z_alpha - noncentrality)
    return power


def n_per_group_proportions(p1, p2, alpha=0.05, power=0.8, two_sided=True):
    """Per-group n for comparing two independent proportions (normal approximation)."""
    _check_probability("alpha", alpha)
    _check_probability("power", power)
    for name, value in (("p1", p1), ("p2", p2)):
        if not 0 <= value <= 1:
            raise ValueError(f"{name} must be between 0 and 1")
    if p1 == p2:
        raise ValueError("p1 and p2 must differ")
    z_alpha = _NORMAL.inv_cdf(1 - alpha / (2 if two_sided else 1))
    z_power = _NORMAL.inv_cdf(power)
    p_bar = (p1 + p2) / 2
    numerator = (
        z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))
        + z_power * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    ) ** 2
    return math.ceil(numerator / (p1 - p2) ** 2)


def inflate_for_dropout(n, dropout):
    """Increase n so the expected analyzable sample is n after the stated dropout fraction."""
    if not 0 <= dropout < 1:
        raise ValueError("dropout must be in [0, 1)")
    return math.ceil(n / (1 - dropout))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("means", "power-means", "props"):
        p = sub.add_parser(name)
        p.add_argument("--alpha", type=float, default=0.05)
        p.add_argument("--one-sided", action="store_true")
        if name != "power-means":
            p.add_argument("--power", type=float, default=0.8)
            p.add_argument("--dropout", type=float, default=0.0)
    sub.choices["means"].add_argument("--d", type=float, required=True, help="Cohen's d")
    sub.choices["power-means"].add_argument("--d", type=float, required=True)
    sub.choices["power-means"].add_argument("--n", type=int, required=True, help="per-group n")
    sub.choices["props"].add_argument("--p1", type=float, required=True)
    sub.choices["props"].add_argument("--p2", type=float, required=True)
    args = parser.parse_args(argv)
    two_sided = not args.one_sided
    if args.command == "means":
        n = n_per_group_means(args.d, args.alpha, args.power, two_sided)
        print(f"n per group: {n}; with dropout: {inflate_for_dropout(n, args.dropout)}")
    elif args.command == "power-means":
        print(f"approximate power: {power_means(args.n, args.d, args.alpha, two_sided):.3f}")
    else:
        n = n_per_group_proportions(args.p1, args.p2, args.alpha, args.power, two_sided)
        print(f"n per group: {n}; with dropout: {inflate_for_dropout(n, args.dropout)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
