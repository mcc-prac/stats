"""Practical 09 - Q01
Question: Perform testing of hypothesis using Sign Test.
"""

from scipy.stats import binom

DATA = [
    1469, 1462, 1634, 1602, 1500, 1463, 1476, 1570, 1544, 1462,
    1487, 1523, 1525, 1548, 1511, 1579, 1620, 1568, 1492, 1649
]
MEDIAN = 1500


def sign_test(data, median, alternative="two-sided"):
    positive = sum(x > median for x in data)
    negative = sum(x < median for x in data)
    n = positive + negative

    if n == 0:
        return 0, 1.0, positive, negative

    if alternative == "two-sided":
        s = min(positive, negative)
        p_value = min(1.0, 2 * binom.cdf(s, n, 0.5))
    elif alternative == "greater":
        p_value = binom.sf(positive - 1, n, 0.5)
    elif alternative == "less":
        p_value = binom.sf(negative - 1, n, 0.5)
    else:
        raise ValueError("alternative must be 'two-sided', 'greater', or 'less'")

    statistic = min(positive, negative)
    return statistic, p_value, positive, negative


def main():
    alternative = input(
        "Enter type of test [two-sided/greater/less]: "
    ).strip().lower() or "two-sided"
    alpha = float(input("Enter value of alpha: "))

    statistic, p_value, positive, negative = sign_test(
        DATA, MEDIAN, alternative
    )

    print("Median:", MEDIAN)
    print("Positive signs:", positive)
    print("Negative signs:", negative)
    print("S-test statistic:", statistic)
    print("p-value:", p_value)
    print("H0 is rejected." if p_value < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
