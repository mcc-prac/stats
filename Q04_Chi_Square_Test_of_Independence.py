"""Practical 09 - Q04
Question: Perform testing of hypothesis for fitting/independence using
Chi-square test.
"""

from scipy.stats import chi2_contingency

DATA = [
    [95, 5],
    [97, 2],
]


def main():
    alpha = float(input("Enter value of alpha: "))

    statistic, p_value, dof, expected = chi2_contingency(DATA)

    print("Observed data:", DATA)
    print("Chi-square test statistic:", statistic)
    print("p-value:", p_value)
    print("Degrees of freedom:", dof)
    print("Expected frequencies:")
    for row in expected:
        print([round(value, 4) for value in row])

    print("H0 is rejected." if p_value < alpha else "H0 is accepted.")


if __name__ == "__main__":
    main()
