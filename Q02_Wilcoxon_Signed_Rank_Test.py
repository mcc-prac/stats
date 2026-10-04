"""Practical 09 - Q02
Question: Perform testing of hypothesis using Wilcoxon Signed Rank Test.
"""

from scipy.stats import wilcoxon

DATA_1 = [21, 34, 3, 45, 80, 54, 37, 36, 33, 40]
DATA_2 = [19, 22, 16, 31, 21, 30, 22, 18, 17, 21]


def main():
    alternative = input(
        "Enter type of test [two-sided/greater/less]: "
    ).strip().lower() or "two-sided"
    alpha = float(input("Enter value of alpha: "))

    result = wilcoxon(DATA_1, DATA_2, alternative=alternative)

    print("Data 1:", DATA_1)
    print("Data 2:", DATA_2)
    print("Wilcoxon signed-rank statistic:", result.statistic)
    print("p-value:", result.pvalue)
    print("H0 is rejected." if result.pvalue < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
