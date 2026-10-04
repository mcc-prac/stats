"""Practical 10 - Q02
Question: Perform testing of hypothesis using Friedman test.

The supplied handwritten page contains the question and an output, but no
input dataset. To avoid inventing source data, this completed program asks
for the groups interactively.
"""

from scipy.stats import friedmanchisquare


def read_group(number):
    values = input(
        f"Enter group {number} values separated by spaces: "
    ).strip()
    group = [float(x) for x in values.split()]
    if not group:
        raise ValueError("Each group must contain at least one value.")
    return group


def main():
    number_of_groups = int(input("Enter number of groups: "))
    if number_of_groups < 3:
        raise ValueError("Friedman test requires at least 3 groups.")

    groups = [read_group(i) for i in range(1, number_of_groups + 1)]

    lengths = {len(group) for group in groups}
    if len(lengths) != 1:
        raise ValueError("All groups must contain the same number of observations.")

    alpha = float(input("Enter value of alpha: "))

    result = friedmanchisquare(*groups)

    print("Friedman test statistic:", result.statistic)
    print("p-value:", result.pvalue)
    print("H0 is rejected." if result.pvalue < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
