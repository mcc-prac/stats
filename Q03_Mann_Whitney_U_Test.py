"""Practical 09 - Q03
Question: Perform testing of hypothesis using Wilcoxon Rank Sum Test
(also called the Mann–Whitney U Test).
"""

from scipy.stats import mannwhitneyu

DATA_1 = [5, 6, 4, 12]
DATA_2 = [3, 6, 4, 2, 1]


def main():
    alternative = input(
        "Enter type of test [two-sided/greater/less]: "
    ).strip().lower() or "two-sided"
    alpha = float(input("Enter value of alpha: "))

    result = mannwhitneyu(
        DATA_1,
        DATA_2,
        alternative=alternative,
    )

    print("Data 1:", DATA_1)
    print("Data 2:", DATA_2)
    print("U-test statistic:", result.statistic)
    print("p-value:", result.pvalue)
    print("H0 is rejected." if result.pvalue < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
