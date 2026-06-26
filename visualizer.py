import matplotlib.pyplot as plt


def create_missing_chart(report):

    missing = report["missing_percent"]

    plt.figure(figsize=(6, 4))

    missing.plot(kind="bar")

    plt.title("Missing Values (%)")
    plt.ylabel("Percentage")

    plt.tight_layout()

    plt.savefig("missing_values.png")

    plt.close()


def create_profit_chart(df):

    profit = df.groupby("Category")["Profit"].sum()

    plt.figure(figsize=(6, 4))

    profit.plot(kind="bar")

    plt.title("Profit by Category")
    plt.ylabel("Profit")

    plt.xlabel("Category")

    plt.tight_layout()

    plt.savefig("profit_by_category.png")

    plt.close()