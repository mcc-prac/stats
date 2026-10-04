"""Practical 06 - Q04
Question: Perform testing of hypothesis for equality of means of two samples using T-test.
The source asks whether the two populations have equal variance.
"""

import numpy as np
from scipy.stats import ttest_ind

SAMPLE_1 = [86, 93, 64, 82, 81, 75, 86, 63, 63]
SAMPLE_2 = [63, 72, 80, 60, 85, 83, 70, 72, 81]


def main():
    data1 = np.asarray(SAMPLE_1, dtype=float)
    data2 = np.asarray(SAMPLE_2, dtype=float)

    print("Sample 1:", data1.tolist())
    print("Sample 2:", data2.tolist())

    equal_var_input = input(
        "Do the populations have equal variance? [yes/no]: "
    ).strip().lower()
    equal_var = equal_var_input in {"yes", "y"}

    alternative = input(
        "Enter type of test [two-sided/greater/less]: "
    ).strip().lower() or "two-sided"
    alpha = float(input("Enter value of alpha: "))

    result = ttest_ind(
        data1,
        data2,
        equal_var=equal_var,
        alternative=alternative,
    )

    print("T-test statistic:", result.statistic)
    print("p-value:", result.pvalue)
    print("Degrees of freedom:", result.df)
    print("H0 is rejected." if result.pvalue < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
