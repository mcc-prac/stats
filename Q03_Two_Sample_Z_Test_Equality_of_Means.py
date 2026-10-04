"""Practical 06 - Q03
Question: Perform testing of hypothesis for equality of mean of two samples using Z-test.
The source program uses known population standard deviations.
"""

import numpy as np
from scipy.stats import norm

SAMPLE_1 = [86, 93, 64, 82, 81, 75, 86, 63, 63]
SAMPLE_2 = [63, 72, 80, 60, 85, 83, 70, 72, 81]


def two_sample_z_test(data1, data2, sigma1, sigma2, alternative="two-sided"):
    data1 = np.asarray(data1, dtype=float)
    data2 = np.asarray(data2, dtype=float)

    z = (np.mean(data1) - np.mean(data2)) / np.sqrt(
        sigma1**2 / len(data1) + sigma2**2 / len(data2)
    )

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
    data1 = SAMPLE_1
    data2 = SAMPLE_2

    print("Sample 1:", data1)
    print("Sample 2:", data2)

    sigma1 = float(input("Enter population standard deviation of sample 1: "))
    sigma2 = float(input("Enter population standard deviation of sample 2: "))
    alternative = input(
        "Enter type of test [two-sided/greater/less]: "
    ).strip().lower() or "two-sided"
    alpha = float(input("Enter value of alpha: "))

    z, p_value = two_sample_z_test(data1, data2, sigma1, sigma2, alternative)

    print("Z-test statistic:", z)
    print("p-value:", p_value)
    print("H0 is rejected." if p_value < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
