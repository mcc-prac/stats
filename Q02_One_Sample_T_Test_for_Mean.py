"""Practical 06 - Q02
Question: T-test of hypothesis for mean.
Aim: Testing of hypothesis for mean.
"""

import numpy as np
from scipy.stats import t

DATA = [12, 15, 14, 16, 13, 15, 14, 16, 15, 14]


def t_test_mean(data, population_mean, alternative="two-sided"):
    data = np.asarray(data, dtype=float)
    n = len(data)
    sample_sd = np.std(data, ddof=1)
    t_stat = (np.mean(data) - population_mean) / (sample_sd / np.sqrt(n))
    df = n - 1

    if alternative == "two-sided":
        p_value = 2 * t.sf(abs(t_stat), df)
    elif alternative == "greater":
        p_value = t.sf(t_stat, df)
    elif alternative == "less":
        p_value = t.cdf(t_stat, df)
    else:
        raise ValueError("alternative must be 'two-sided', 'greater', or 'less'")

    return t_stat, p_value, df


def main():
    data = DATA
    mu = float(input("Enter population mean: "))
    alternative = input(
        "Enter type of test [two-sided/greater/less]: "
    ).strip().lower() or "two-sided"
    alpha = float(input("Enter value of alpha: "))

    t_stat, p_value, df = t_test_mean(data, mu, alternative)

    print("T-test statistic:", t_stat)
    print("p-value:", p_value)
    print("Degrees of freedom:", df)
    print("H0 is rejected." if p_value < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
