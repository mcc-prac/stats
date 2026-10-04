"""Practical 10 - Q03
Question: Perform testing of hypothesis for Mood median test.
"""

from scipy.stats import median_test

GROUP_1 = [1, 14, 19, 12, 11, 15, 20, 5, 21, 15, 15, 15, 28, 31, 6]
GROUP_2 = [16, 17, 14, 10, 31, 22, 26, 24, 27, 32, 16, 8, 12, 11]


def main():
    alpha = float(input("Enter value of alpha: "))

    statistic, p_value, median, table = median_test(GROUP_1, GROUP_2)

    print("Median:", median)
    print("Mood median test statistic:", statistic)
    print("p-value:", p_value)
    print("Contingency table:")
    print(table)
    print("H0 is rejected." if p_value < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
