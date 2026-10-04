"""Practical 07 - Q01
Question: Perform testing of hypothesis of variance of one sample using
Chi-square test.
"""

import numpy as np
from scipy.stats import chi2

DATA = [88, 42, 43, 50, 48, 45, 52, 50]


def chi_square_variance_test(data, population_variance, alternative="two-sided"):
    data = np.asarray(data, dtype=float)
    n = len(data)
    sample_variance = np.var(data, ddof=1)
    statistic = (n - 1) * sample_variance / population_variance
    df = n - 1

    if alternative == "two-sided":
        p_value = 2 * min(chi2.cdf(statistic, df), chi2.sf(statistic, df))
        p_value = min(p_value, 1.0)
    elif alternative == "greater":
        p_value = chi2.sf(statistic, df)
    elif alternative == "less":
        p_value = chi2.cdf(statistic, df)
    else:
        raise ValueError("alternative must be 'two-sided', 'greater', or 'less'")

    return statistic, p_value, df


def main():
    population_variance = float(input("Enter the population variance: "))
    alternative = input(
        "Enter type of test [two-sided/right/left]: "
    ).strip().lower() or "two-sided"
    alternative = {"right": "greater", "left": "less"}.get(alternative, alternative)
    alpha = float(input("Enter value of alpha: "))

    statistic, p_value, df = chi_square_variance_test(
        DATA, population_variance, alternative
    )

    print("Data:", DATA)
    print("Chi-square test statistic:", statistic)
    print("p-value:", p_value)
    print("Degrees of freedom:", df)
    print("H0 is rejected." if p_value < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
