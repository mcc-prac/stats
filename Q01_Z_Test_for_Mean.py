"""Practical 06 - Q01
Question: Test of hypothesis for mean using Z-test.
Aim: Testing of hypothesis for mean.
"""

import numpy as np
from scipy.stats import norm

DATA = [12, 15, 14, 16, 13, 15, 14, 16, 15, 14]


def z_test_mean(data, population_mean, population_sd, alternative="two-sided"):
    data = np.asarray(data, dtype=float)
    n = len(data)
    z = (np.mean(data) - population_mean) / (population_sd / np.sqrt(n))

    if alternative == "two-sided":
        p_value = 2 * norm.sf(abs(z))
    elif alternative == "greater":
        p_value = norm.sf(z)
    elif alternative == "less":
        p_value = norm.cdf(z)
    else:
        raise ValueError("alternative must be 'two-sided', 'greater', or 'less'")

    return z, p_value


def main():
    data = DATA
    mu = float(input("Enter population mean: "))
    sigma = float(input("Enter population standard deviation: "))
    alternative = input(
        "Enter type of test [two-sided/greater/less]: "
    ).strip().lower() or "two-sided"
    alpha = float(input("Enter value of alpha: "))

    z, p_value = z_test_mean(data, mu, sigma, alternative)

    print("Z-test statistic:", z)
    print("p-value:", p_value)
    print("H0 is rejected." if p_value < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
