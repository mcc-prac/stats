"""Practical 07 - Q02
Question: Perform testing of hypothesis for variance of two samples using
F-test.
"""

import numpy as np
from scipy.stats import f

SAMPLE_1 = [86, 93, 64, 82, 81, 75, 86, 63, 63]
SAMPLE_2 = [63, 72, 80, 60, 85, 83, 70, 72, 81]


def f_test_variance(data1, data2, alternative="two-sided"):
    data1 = np.asarray(data1, dtype=float)
    data2 = np.asarray(data2, dtype=float)

    n1, n2 = len(data1), len(data2)
    var1 = np.var(data1, ddof=1)
    var2 = np.var(data2, ddof=1)

    statistic = var1 / var2
    df1, df2 = n1 - 1, n2 - 1

    if alternative == "two-sided":
        p_value = 2 * min(
            f.cdf(statistic, df1, df2),
            f.sf(statistic, df1, df2),
        )
        p_value = min(p_value, 1.0)
    elif alternative == "greater":
        p_value = f.sf(statistic, df1, df2)
    elif alternative == "less":
        p_value = f.cdf(statistic, df1, df2)
    else:
        raise ValueError("alternative must be 'two-sided', 'greater', or 'less'")

    return statistic, p_value, df1, df2


def main():
    alternative = input(
        "Enter type of test [two-sided/greater/less]: "
    ).strip().lower() or "two-sided"
    alpha = float(input("Enter value of alpha: "))

    statistic, p_value, df1, df2 = f_test_variance(
        SAMPLE_1, SAMPLE_2, alternative
    )

    print("Sample 1:", SAMPLE_1)
    print("Sample 2:", SAMPLE_2)
    print("F-test statistic:", statistic)
    print("p-value:", p_value)
    print("Degrees of freedom:", (df1, df2))
    print("H0 is rejected." if p_value < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
