"""Practical 10 - Q01
Question: WAP for Kruskal's algorithm.
Statistical operation shown in the source: Kruskal-Wallis hypothesis test.
"""

from scipy.stats import kruskal

GROUP_1 = [23, 41, 54, 66, 87]
GROUP_2 = [45, 55, 60, 70, 72]
GROUP_3 = [20, 80, 84, 40, 44]


def main():
    alpha = float(input("Enter value of alpha: "))

    result = kruskal(GROUP_1, GROUP_2, GROUP_3)

    print("Group 1:", GROUP_1)
    print("Group 2:", GROUP_2)
    print("Group 3:", GROUP_3)
    print("Test statistic:", result.statistic)
    print("p-value:", result.pvalue)
    print("H0 is rejected." if result.pvalue < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
