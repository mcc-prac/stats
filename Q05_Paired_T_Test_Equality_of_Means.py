"""Practical 06 - Q05
Question: Perform testing of hypothesis for equality of two samples using
T-test (dependent/paired).
"""

from scipy.stats import ttest_rel

BEFORE = [12, 14, 1, 8, 7, 10, 3, 0, 5, 6]
AFTER = [15, 16, 10, 7, 5, 12, 10, 8, 2, 8]


def main():
    alternative = input(
        "Enter type of test [two-sided/greater/less]: "
    ).strip().lower() or "two-sided"
    alpha = float(input("Enter value of alpha: "))

    result = ttest_rel(BEFORE, AFTER, alternative=alternative)

    print("Before:", BEFORE)
    print("After :", AFTER)
    print("Paired T-test statistic:", result.statistic)
    print("p-value:", result.pvalue)
    print("Degrees of freedom:", len(BEFORE) - 1)
    print("H0 is rejected." if result.pvalue < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
